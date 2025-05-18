from django.views.generic import FormView, ListView, View


class PublishedMixin(View):
    def get_queryset(self):
        """
        Override get method here to allow us to access the request user
        """
        return self.model.objects.published(user=self.request.user)


class FormFilterListView(ListView, FormView):
    """
    Adds a filter form to the view so we can filter the queryset in a ListView. This should be the
    last item in the MRO.
    """

    form_class = None

    def get_form_class(self):
        if not self.form_class:
            raise NotImplementedError("form_class must be defined")
        return self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"data": self.request.GET or None})
        return kwargs

    def get(self, request, *args, **kwargs):
        """
        A slight mimic of POST where we handle the form conditionals. We use GET as that's how our
        form is being submitted on the frontend. If the form has been submitted we filter the
        queryset, otherwise we return the full queryset as defined in get_queryset() and render the
        blank form.
        """
        form = self.get_form()

        if form.is_valid():
            self.object_list = form.filter_queryset(self.get_queryset())
        else:
            self.object_list = self.get_queryset()

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "form": self.get_form(),
                self.context_object_name: self.object_list,
            }
        )
        return context

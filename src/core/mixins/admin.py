READONLY_FIELDS = ["created_at", "updated_at"]

READONLY_FIELDSET = ("Timestamps", {"classes": ("collapse",), "fields": READONLY_FIELDS})

PUBLISHING_FIELDSET = ("Publishing", {"fields": ["is_published", "publish_at"]})

META_FIELDSET = ("Meta Data", {"fields": ["meta_title", "meta_description"]})

from django.core.files.uploadedfile import SimpleUploadedFile

import pytest
from filer.models.filemodels import File


def create_test_filer_file():
    image_name = "test_file.pdf"
    file_obj = SimpleUploadedFile(name=image_name, content=b"test", content_type="application/pdf")
    image = File(original_filename=image_name, file=file_obj)
    return image


@pytest.fixture
def file_instance():
    return create_test_filer_file()

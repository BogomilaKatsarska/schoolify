from django.db import models


class CreatedAndUpdatedInfoMixIn(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )


class DisabledFormFieldsMixin:
    disabled_attr_name = 'readonly'
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widgetd.attrs[self.disabled_attr_name] = self.disabled_attr_name

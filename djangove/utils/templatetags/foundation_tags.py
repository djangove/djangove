from django import template
from django.forms import CheckboxInput
from django.template import Context
from django.template.loader import get_template

register = template.Library()


@register.filter
def as_foundation(form):
    template = get_template("utils/tags/foundation/form.html")
    c = Context({"form": form})
    return template.render(c)


@register.inclusion_tag('utils/tags/foundation/foundation_form_field.html')
def render_field(field):
    """
    Use this need tag to get more control over the layout of your forms

    {% render_field form.my_field %}
    """
    return {'field': field}


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput(
    ).__class__.__name__

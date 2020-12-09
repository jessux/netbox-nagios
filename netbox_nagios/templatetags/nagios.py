from django import template  # pylint: disable=import-error

register = template.Library()  # pylint: disable=invalid-name


@register.filter(is_safe=True)
def nagios_status_color(value):
    local_colors = {0: "success", 1: "warning", 2: "danger", 3: "info"}
    return local_colors.get(int(value), "default")


@register.filter(is_safe=True)
def nagios_status_string(value):
    strings = {0: "UP",2: "DOWN", 3: "UNREACHABLE"}
    return strings.get(int(value), "NOT FOUND")

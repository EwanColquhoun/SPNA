from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """Custom widget for the edit article template"""
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('Change')
    template_name = 'spna_admin/custom_widget_templates/custom_clearable_file_input.html'

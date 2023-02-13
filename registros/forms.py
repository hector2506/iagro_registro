from bootstrap_datepicker_plus.widgets import DatePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, Submit
from django.forms import CharField, Form, ModelForm

from registros.models import AbateDiario


class AbateDiarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AbateDiarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-abate-diario-form"
        self.helper.form_method = "post"
        self.helper.form_action = "registros:test"

        self.helper.layout = Layout(
            Div(
                Div(
                    HTML('<h3 class="card-header-text">Abate Diário</h3>'),
                    css_class="card-header",
                ),
                Div("dia", css_class="mb-3"),
                HTML("<hr>"),
                HTML('<h5 class="card-header-text">Cortes de Suínos</h5>'),
                Field(
                    "cortes_suinos",
                    css_class="form-control",
                    type="hidden",
                ),
                Div(
                    Div(
                        Div(
                            HTML(
                                "<div class='mb-3'>"
                                "<label class='form-label'> Peso do Corte </label>"
                                "<input type='number' name='peso-suinos' min='0.0' step='0.5' class='numberinput form-control peso-suinos'>"
                                "</div>"
                            ),
                            css_class="col",
                        ),
                        Div(
                            HTML(
                                "<div class='mb-3'>"
                                "<label class='form-label'> Quantidade de Cortes </label>"
                                "<input type='number' name='quant-suinos' min='1' class='numberinput form-control quant-suinos'>"
                                "</div>"
                            ),
                            css_class="col",
                        ),
                        style="justify-content: space-between",
                        css_class="row g-3",
                        name="array-suinos",
                    ),
                    id="cortes-suinos",
                ),
                HTML(
                    f"<a class='btn btn-info add-suino' id='add-suino' onclick=add_input('cortes-suinos')><i class='fa fa-plus'></i> Adicionar Outro Corte</a>",
                ),
                HTML("<hr>"),
                HTML('<h5 class="card-header-text">Cortes de Carneiros</h5>'),
                Field(
                    "cortes_carneiros",
                    css_class="form-control",
                    type="hidden",
                ),
                Div(
                    Div(
                        Div(
                            HTML(
                                "<div class='mb-3'>"
                                "<label class='form-label'> Peso do Corte </label>"
                                "<input type='number' name='peso-carneiros' min='0.0' step='0.5' class='numberinput form-control peso-carneiros'>"
                                "</div>"
                            ),
                            css_class="col",
                        ),
                        Div(
                            HTML(
                                "<div class='mb-3'>"
                                "<label class='form-label'> Quantidade de Cortes </label>"
                                "<input type='number' name='quant-carneiros' min='1' class='numberinput form-control quant-carneiros'>"
                                "</div>"
                            ),
                            css_class="col",
                        ),
                        style="justify-content: space-between",
                        css_class="row g-3",
                        name="array-carneiros",
                    ),
                    id="cortes-carneiros",
                ),
                HTML(
                    f"<a class='btn btn-info add-carneiro' id='add-carneiro' onclick=add_input('cortes-carneiros')><i class='fa fa-plus'></i> Adicionar Outro Corte</a>",
                ),
                HTML("<hr>"),
            ),
            Submit(
                "Sign in",
                "Registrar",
                css_class="btn btn-success",
            ),
        )

    class Meta:
        model = AbateDiario
        fields = ["dia", "cortes_suinos", "cortes_carneiros"]
        widgets = {
            "dia": DatePickerInput(options={"format": "MM/DD/YYYY"}),
        }


class NameForm(Form):
    your_name = CharField(label="Your name", max_length=100)

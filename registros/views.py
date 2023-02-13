from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView

from registros.models import AbateDiario

from .forms import AbateDiarioForm


class IndexView(ListView):
    template_name = "registros/listagem_abates.html"
    context_object_name = "abate_lista"
    queryset = AbateDiario.objects.order_by("dia")


class TestFormView(FormView):
    template_name = "registros/cadastro_abate.html"
    form_class = AbateDiarioForm
    success_url = reverse_lazy("registros:index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

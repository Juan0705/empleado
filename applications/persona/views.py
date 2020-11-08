from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,

)
# models
from .models import Empleado
# forms
from .forms import EmpleadoForm


class InicioView(TemplateView):
    template_name = "inicio.html"

# 1.- Listar todos los empleados de la empresa


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    # model = Empleado # ya no es necesario al ocupar el metodo get_queryset
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        lista = Empleado.objects.filter(
            # __icontains:busca la cadena similar (jorge = j)
            first_name__icontains=palabra_clave
        )
        return lista  # retorna todos los elementos porque full_name siempre tiene un vacio


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    # model = Empleado # ya no es necesario al ocupar el metodo get_queryset
    context_object_name = 'empleados'
    model = Empleado


# 2.- Listar a todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo
class ListByAreaEmpleado(ListView):
    """lista empleados de una area"""
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):  # filtro
        # el codigo que yo quiero
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista


# 4.- Listar a los empleados por palabra clave
class ListEmpleadosByKword(ListView):
    """lista empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista


# 5.- Listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)
        print(empleado.habilidades.all())
        return []


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # toot un proceso
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = 'persona/success.html'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    ############################################################
    '''
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    '''
    # al usar un forms se omiten los campos fields obtenidos del modelo
    form_class = EmpleadoForm
    #############################################################
    #fields = ('__all__')
    # success_url = '.' # al agregar redirecciona a la misma pagina
    # success_url = '/success' # al agregar redirecciona a SuccessView
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):  # intercepta el formulario
        # Logica del proceso
        # guarda en esta variable el contenido del formulario
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + \
            empleado.last_name  # define un valor para el nombre completo
        empleado.save()  # guarda el valor asignado en la bd
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('****************METODO POST***********************')
        print('**************************************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):  # intercepta el formulario
        # Logica del proceso
        print('**********************METODO FORM VALID*****************')
        print('********************************************************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

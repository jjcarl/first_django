from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main.models import State, StateCapital, City
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from main.forms import CitySearchForm, CreateCityForm
from django.views.generic import FormView
from django.core.mail import send_mail

# Create your views here.


def template_view(request):
    context = {}
    state_city = {}

    states = State.objects.all()

    for state in states:
        cities = state.city_set.filter(name__startswith="A")

        state.name = {state.name: cities}

        state_city.update(state.name)

    context['states'] = state_city

    return render_to_response('template_view.html', context, context_instance=RequestContext(request))


def first_view(request, starts_with=None):

    states = State.objects.all()

    text_string = ''

    for state in states:
        cities = state.city_set.filter(name__startswith="%s" % starts_with)
        for city in cities:
            text_string += "State: %s, City: %s <br>" % (state, city.name)

    return HttpResponse(text_string)


@csrf_exempt
def get_post(request):

    if request.method == "GET":

        city_state_string = """

        <form action="/get_post/" method="POST">

        State:
        </br>
        <input type="text" name="state" />
        </br>

        City:
        </br>
        <input type="text" name="city" />
        </br>
        <input type="submit" value="Submit" />

        </form>
        """

        return HttpResponse(city_state_string)

    if request.method == "POST":

        city_state_string = """

        <form action="/get_post/" method="POST">

        State:
        </br>
        <input type="text" name="state" />
        </br>

        City:
        </br>
        <input type="text" name="city" />
        </br>
        <input type="submit" value="Submit" />

        </form>
        """

        get_state = request.POST.get('state', None)

        get_city = request.POST.get('city', None)

        states = State.objects.filter(name__startswith="%s" % get_state)

        for state in states:
            cities = state.city_set.filter(name__startswith="%s" % get_city)
            for city in cities:
                city_state_string += "<b>%s</b> %s </br>" % (state, city.name)

        response = city_state_string

        return HttpResponse(response)


class GetPost(View):

    form = """

        <form action="/GetPost/" method="POST">

        State:
        </br>
        <input type="text" name="state" />
        </br>

        City:
        </br>
        <input type="text" name="city" />
        </br>
        <input type="submit" value="Submit" />

        </form>
        """

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.form)

    def post(self, request, *args, **kwargs):

        get_state = request.POST.get('state', None)
        get_city = request.POST.get('city', None)

        states = State.objects.filter(name__startswith="%s" % get_state)

        for state in states:
            cities = state.city_set.filter(name__startswith="%s" % get_city)
            for city in cities:
                self.form += "<b>%s</b> %s </br>" % (state, city.name)

        response = self.form

        return HttpResponse(response)


class StateListView(ListView):
    model = State
    template_name = "state_list.html"
    context_object_name = "state_list"


class CityDetailView(DetailView):
    model = City
    template_name = "city_detail.html"
    context_object_name = "city"


def city_search(request):
    request_context = RequestContext(request)

    context = {}

    if request.method == 'POST':
        form = CitySearchForm(request.POST)
        context["form"] = form

        if form.is_valid():
            name = "%s" % form.cleaned_data['name']
            state = form.cleaned_data['state']

            context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

            context['valid'] = "is valid"

            return render_to_response("city_search.html", context, context_instance=request_context)
        else:
            context['valid'] = form.errors

            return render_to_response("city_search.html", context, context_instance=request_context)

    else:
        form = CitySearchForm()
        context["form"] = form

        return render_to_response("city_search.html", context, context_instance=request_context)


def city_create(request):
    request_context = RequestContext(request)

    context = {}

    if request.method =='POST':
        form = CreateCityForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()

            context['valid'] = "Is valid"

            return render_to_response("city_create.html", context, context_instance=request_context)

        else:
            context['valid'] = form.errors

            return render_to_response("city_create.html", context, context_instance=request_context)

    else:
        form = CreateCityForm()
        context['form'] = form

        return render_to_response("city_create.html", context, context_instance=request_context)


class CitySearchView(FormView):
    template_name = 'city_search.html'
    form_class = CitySearchForm

    def form_valid(self, form):
        request_context = RequestContext(self.request)

        context = {}

        name = form.cleaned_data['name']
        state = form.cleaned_data['state']

        context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

        send_mail('City name starts with %s' % name, 'The state is %s.' % state, 'jcarl9000@gmail.com', ['jcarl9000@gmail.com'], fail_silently=False)

        return render_to_response("city_create.html", context, context_instance=request_context)

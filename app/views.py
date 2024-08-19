import requests
from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        servicess = requests.get("http://127.0.0.1:8000/services/").json()
        context = {"servicess": servicess}
        return render(request, 'service.html', context)


class IndexView(View):
    def get(self, request):
        testimonials = requests.get("http://127.0.0.1:8000/clients/").json()
        context = {"testimonials": testimonials}
        return render(request, 'index.html', context)


class AboutView(View):
    def get(self, request):
        feature = requests.get("http://127.0.0.1:8000/features/").json()
        teams = requests.get("http://127.0.0.1:8000/advisers/").json()
        context = {"feature": feature,
                   "teams": teams}

        return render(request, 'about.html', context)


class ServicesView(View):
    def get(self, request):
        servicess = requests.get("http://127.0.0.1:8000/services/").json()
        client = requests.get("http://127.0.0.1:8000/clients/").json()
        context = {"servicess": servicess,
                   "client": client}
        return render(request, 'service.html', context)


class AdvisersView(View):
    def get(self, request):
        adviser = requests.get("http://127.0.0.1:8000/advisers/").json()
        context = {"adviser": adviser}
        return render(request, 'team.html', context)


class BlogView(View):
    def get(self, request):
        blogs = requests.get("http://127.0.0.1:8000/blogs/").json()
        context = {"blogs": blogs}
        return render(request, 'blog.html', context)


class FeaturesView(View):
    def get(self, request):
        feature = requests.get("http://127.0.0.1:8000/features/").json()
        context = {"feature": feature}
        return render(request, 'features.html', context)


class ClientsView(View):
    def get(self, request):
        client = requests.get("http://127.0.0.1:8000/clients/").json()
        context = {"clients": client}
        return render(request, 'clients.html', context)




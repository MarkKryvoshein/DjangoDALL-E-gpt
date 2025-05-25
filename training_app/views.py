import os

from django.shortcuts import render, redirect

from django.contrib.auth import logout

from training_app.forms import PromptForm

from template.settings import API_KEY

from training_app.forms import CustomUserCreationForm as registrationForm

from .models import QueryHistory

import openai

client = openai.OpenAI(api_key=API_KEY)


def mainPage(request):
    response_text = None
    response_image = None

    if request.method == 'POST':
        form = PromptForm(request.POST)
        # is_valid
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            completion = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = completion.choices[0].message.content
            image_result = client.images.generate(
                model="dall-e-3",
                prompt=prompt
            )

            response_image = image_result.data[0].url
            if request.user.is_authenticated:
                QueryHistory.objects.create(
                    user=request.user,
                    query=prompt,
                    response_text=response_text,
                    response_image=response_image
                )
    else:
        form = PromptForm()
    return render(request, 'index.html', {
        "response_image": response_image,
        "response_text": response_text,
        "form": form
    })


def signUp(request):
    if request.method == "POST":
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('..')
        return render(request, 'registration/signup.html', {'form': form})
    else:
        form = registrationForm()
        return render(request, 'registration/signup.html', {'form': form})


def logOut(request):
    if request.method == "POST":
        logout(request)
        return redirect('..')
    else:
        # При GET запиті, можеш або показати підтвердження, або просто редірект
        return render(request, 'registration/logout.html', {"form": registrationForm()})


# Create your views here.




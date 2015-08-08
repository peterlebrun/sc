from django.shortcuts import render
from .models import Prompt, Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.

def home(request):
    context = {
        'prompt': Prompt.objects.filter().order_by('?').first(),
    }

    return render(request, 'se/index.html', context)

@csrf_exempt
def write_response(request):
    context = { 'success': True }

    r = Response.objects.create(
        content = request.POST['response_content'],
        prompt  = Prompt.objects.get(id = request.POST['prompt_id']),
        date    = datetime.datetime.now()
    )

    r.save()

    if request.POST['new_prompt_id']:
        p = Prompt.objects.get(id = request.POST['new_prompt_id'])
        context['prompt_content'] = p.content
        context['prompt_id']      = p.id

    return JsonResponse(context)

def multi_prompt(request):
    return render(request, 'se/multi_prompt.html')

def respond_multi(request):
    prompts = [s.split() for s in request.POST['prompts'].splitlines()]

    prompt_ids = []

    for prompt in prompts:
        p = Prompt.objects.create(
            content = prompt,
            date    = datetime.datetime.now()
        )
        p.save()
        prompt_ids.append(p.id)

    initial_prompt = Prompt.objects.get(id = prompt_ids[0])

    context = {
        'prompt_ids' : prompt_ids,
        'initial_prompt_id' : initial_prompt.id,
        'initial_prompt_content' : initial_prompt.content,
    }

    return render(request, 'se/respond_multi.html', context)

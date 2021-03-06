from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

# Models
from centers.models import Center

# Forms
from centers.forms import CenterForm


@require_http_methods(["GET"])
def centers(request):
    centers = Center.objects.all()
    return render(request, "centers/centers.html", {
        'centers': centers
    })


@require_http_methods(["GET"])
def center(request, pk):
    center = get_object_or_404(Center, pk=pk)
    return render(request, "centers/center.html", {
        'center': center
    })


@require_http_methods(["GET", "POST"])
def center_create(request):
    form = CenterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("centers")
    return render(request, "centers/form.html", {
        'form': form
    })


@require_http_methods(["GET", "POST"])
def center_update(request, pk):
    center = get_object_or_404(Center, pk=pk)
    form = CenterForm(request.POST or None, instance=center)

    if form.is_valid():
        form.save()
        return redirect("centers")
    return render(request, "centers/form.html", {
        'form': form
    })


@require_http_methods(["POST"])
def center_delete(request, pk):
    center = get_object_or_404(Center, pk=pk)
    if request.method == "POST":
        center.delete()
        return redirect("centers")
    return redirect("centers")

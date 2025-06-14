from django.shortcuts import render, redirect
from .linkedlist import LinkedList

linked_list = LinkedList()

def home(request):
    context = {
        'linked_list': linked_list.print_list()
    }
    return render(request, 'home.html', context)

def add_node(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        if value:
            linked_list.add_node(value)
            context = {
                'linked_list': linked_list.print_list(),
                'message': f"✅ Node '{value}' added successfully.",
                'message_type': "success"
            }
            return render(request, 'home.html', context)
    return redirect('home')

def delete_node(request):
    message = ''
    message_type = 'danger'
    if request.method == 'POST':
        try:
            index = int(request.POST.get('index'))
            deleted = linked_list.delete_nth_node(index)
            message = f"🗑️ Node at position {index} deleted successfully."
            message_type = "success"
        except Exception as e:
            message = f"❌ Error: {str(e)}"
            message_type = "danger"

    context = {
        'linked_list': linked_list.print_list(),
        'message': message,
        'message_type': message_type
    }
    return render(request, 'home.html', context)

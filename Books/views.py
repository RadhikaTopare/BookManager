# books/views.py
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.db.models import Count, Avg

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
    return render(request, 'login.html')

# User Logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')


# Create a new book
@login_required
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)  # Create the book instance without saving
        book.user = request.user        # Assign the logged-in user to the book's user field
        book.save() 
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})

@login_required
def dashboard(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return redirect('dashboard')
    total_books = Book.objects.filter(user=request.user).count()
    books_read = Book.objects.filter(user=request.user, status='R').count()
    genre_stats = Book.objects.values('genre').annotate(count=Count('genre')).order_by('-count')
    genre_distribution = Book.objects.filter(user=request.user).values('genre').annotate(count=Count('genre'))
    avg_rating = Book.objects.filter(user=request.user).aggregate(Avg('rating'))
    books = Book.objects.all()
    context = {
        'total_books': total_books,
        'books_read': books_read,
        'genre_stats': genre_stats,
        'genre_distribution': genre_distribution,
        'avg_rating': avg_rating['rating__avg'],
        'books': books,
    }
    return render(request, 'dashboard.html', context)
# List all books
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

@login_required
def book_delete(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
    return redirect('book_list') 

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Get the specific book by primary key
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after updating
    else:
        form = BookForm(instance=book)  # Pre-fill the form with the book data

    return render(request, 'book_update.html', {'form': form, 'book': book})

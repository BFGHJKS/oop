import java.util.ArrayList;
import java.util.Scanner;

class Book {
    String title;
    String author;
    String isbn;

    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
    }
}

class Library {
    ArrayList<Book> books;

    public Library() {
        this.books = new ArrayList<>();
    }

    public void addBook(String title, String author, String isbn) {
        Book newBook = new Book(title, author, isbn);
        books.add(newBook);
        System.out.println("Book '" + title + "' added to the library.");
    }

    public void removeBook(String isbn) {
        for (Book book : books) {
            if (book.isbn.equals(isbn)) {
                books.remove(book);
                System.out.println("Book '" + book.title + "' removed from the library.");
                return;
            }
        }
        System.out.println("Book with ISBN " + isbn + " not found in the library.");
    }

    public void displayBooks() {
        if (books.isEmpty()) {
            System.out.println("The library is empty.");
        } else {
            System.out.println("Books in the library:");
            for (Book book : books) {
                System.out.println("Title: " + book.title + ", Author: " + book.author + ", ISBN: " + book.isbn);
            }
        }
    }
}

public class biblio {
    public static void main(String[] args) {
        Library library = new Library();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of books to add: ");
        int numBooks = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < numBooks; i++) {
            System.out.print("Enter the title of the book: ");
            String title = scanner.nextLine();
            System.out.print("Enter the author of the book: ");
            String author = scanner.nextLine();
            System.out.print("Enter the ISBN of the book: ");
            String isbn = scanner.nextLine();
            library.addBook(title, author, isbn);
        }

        library.displayBooks();

        System.out.print("Enter the ISBN of the book to remove: ");
        String isbnToRemove = scanner.nextLine();
        library.removeBook(isbnToRemove);

        library.displayBooks();

        scanner.close();
    }
}

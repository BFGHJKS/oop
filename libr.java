import java.util.ArrayList;
import java.util.Scanner;

class Book {
    private String title;
    private String author;
    private String ISBN;

    public Book(String title, String author, String ISBN) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getISBN() {
        return ISBN;
    }

    @Override
    public String toString() {
        return "Title: " + title + "\nAuthor: " + author + "\nISBN: " + ISBN + "\n";
    }
}

class Library {
    private ArrayList<Book> books;

    public Library() {
        this.books = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
        System.out.println("Book added to the library successfully.\n");
    }

    public void removeBook(String ISBN) {
        for (Book book : books) {
            if (book.getISBN().equals(ISBN)) {
                books.remove(book);
                System.out.println("Book removed from the library successfully.\n");
                return;
            }
        }
        System.out.println("Book with ISBN " + ISBN + " not found in the library.\n");
    }

    public void displayAllBooks() {
        if (books.isEmpty()) {
            System.out.println("The library is empty.\n");
        } else {
            System.out.println("All Books in the Library:\n");
            for (Book book : books) {
                System.out.println(book);
            }
        }
    }
}

public class Libr {
    public static void main(String[] args) {
        Library library = new Library();
        Scanner scanner = new Scanner(System.in);

        int choice;
        do {
            System.out.println("Menu:");
            System.out.println("1. Add a Book");
            System.out.println("2. Remove a Book");
            System.out.println("3. Display all Books");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter Book Title (Write _ as a space): ");
                    String title = scanner.next();
                    System.out.print("Enter Author Name (Write _ as a space): ");
                    String author = scanner.next();
                    System.out.print("Enter ISBN: ");
                    String ISBN = scanner.next();
                    Book newBook = new Book(title, author, ISBN);
                    library.addBook(newBook);
                    break;
                case 2:
                    System.out.print("Enter ISBN of the Book to be removed: ");
                    ISBN = scanner.next();
                    library.removeBook(ISBN);
                    break;
                case 3:
                    library.displayAllBooks();
                    break;
                case 4:
                    System.out.println("Exiting \n");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a valid option.\n");
                    break;
            }
        } while (choice != 4);

        scanner.close();
    }
}

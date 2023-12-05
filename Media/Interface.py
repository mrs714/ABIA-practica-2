import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import csv
from io import BytesIO
import requests
import sys

sys.path.insert(0, './JocsDeProva')

from Automator import BookGraphGenerator

class BookSelectorApp:
    def __init__(self, root, parallels = True):
        self.root = root
        self.root.title("Book Selector")
        self.books = self.read_books_from_dataset("./Media/books.csv", parallels)
        self.selected_books = []
        self.max = 0
        self.create_interface()

    def read_books_from_dataset(self, file_path, parallelsbool = True):
        books = []
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                title, predecessors, parallels, pages, author, series, image_url = map(str.strip, row)
                if not parallelsbool:
                    parallels = ""
                books.append({
                    "title": title,
                    "author": author,
                    "series": series,
                    "predecessors": predecessors.split(","),
                    "parallels": parallels.split(","),
                    "pages": pages,
                    "image_url": image_url,
                    "selected": False,
                    "needed": False,
                    "read": False,
                })
        return books

    def create_interface(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)

        for row in range(self.max):
            self.root.grid_rowconfigure(row, weight=0)
        for col in range(1, 13):
            self.root.grid_columnconfigure(col, weight=0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        

        canvas = tk.Canvas(main_frame)
        canvas.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.grid(row=0, column=1, padx=0, pady=5, sticky=tk.NS)
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)
        self.populate_books_frame(frame)

        frame.bind("<Configure>", lambda event, canvas=canvas: self.on_frame_configure(canvas))

        self.selected_books_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40, height=10)
        self.selected_books_listbox.grid(row=0, column=1, padx=10, pady=10, rowspan=2, sticky=tk.NSEW)

        remove_button = ttk.Button(self.root, text="Remove", command=self.remove_selected_book)
        remove_button.grid(row=2, column=1, padx=10, pady=5, sticky=tk.NSEW)

        plan_button = ttk.Button(self.root, text="Create plan", command=self.create_lists)
        plan_button.grid(row=3, column=1, padx=10, pady=5, sticky=tk.NSEW)

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=0)

        main_frame.grid_rowconfigure(0, weight=1)
        self.update_selected_books_listbox()


    def populate_books_frame(self, frame):
        for i, book in enumerate(self.books):
            image_url = book['image_url']
            title = book['title']
            try:
                img = Image.open(image_url)
            except:
                img = Image.open("./Media/Images/noimage.png")
            img = img.resize((100, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            label = ttk.Label(frame, image=photo, text=title, compound=tk.BOTTOM, cursor="hand2", style="Book.TLabel")
            label.grid(row=i // 6, column=i % 6, padx=10, pady=10)

            label.photo = photo  # Keep a reference to the photo to prevent garbage collection

            label.bind("<Button-1>", lambda event, title=title: self.toggle_select_book(title, frame))

        for row in range((len(self.books) - 1) // 6 + 1):
            frame.grid_rowconfigure(row, weight=1)
        for col in range(6):
            frame.grid_columnconfigure(col, weight=1)
        self.frame2 = frame

    def on_frame_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def toggle_select_book(self, title, frame):
        for book in self.books:
            if book['title'] == title:
                book['selected'] = not book['selected']
                self.update_book_label(title, frame)
                self.update_selected_books_listbox()
                break

    def update_book_label(self, title, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget("text") == title:
                selected_color = "lightblue" if any(book['selected'] for book in self.books if book['title'] == title) else "white"
                widget.configure(style="Book.TLabel", background=selected_color)
        for book in self.books:
            if book['title'] == title:
                self.check_needed(book)
        self.update_selected_books_listbox()


    def update_selected_books_listbox(self):
        self.selected_books_listbox.delete(0, tk.END)
        for book in self.books:
            if book['selected'] or book['needed']:
                self.selected_books_listbox.insert(tk.END, book['title'])

    def remove_selected_book(self):
        selected_index = self.selected_books_listbox.curselection()
        if selected_index:
            selected_title = self.selected_books_listbox.get(selected_index)
            for book in self.books:
                if book['title'] == selected_title:
                    book['selected'] = False
                    self.update_book_label(selected_title, self.frame2)
                    break
            self.update_selected_books_listbox()

    def print_selected_books(self):
        print("Selected Books:")
        for book in self.books:
            if book['selected']:
                print(f"- {book['title']}")
                self.print_selected_with_parallels(book)

    def print_selected_with_parallels(self, book):
        for pred in book['predecessors']:
            if pred != '':
                print(f"- {pred}")
                for predpred in self.books:
                    if predpred['title'] == pred:
                        self.print_selected_with_parallels(predpred)
                        predpred['selected'] = True
                self.update_selected_books_listbox()

    def get_full_predecessors(self, book):
        preds = []
        for pred in book['predecessors']:
            if pred != '':
                for predpred in self.books:
                    if predpred['title'] == pred:
                        self.get_full_predecessors(predpred)
                        preds.append((  predpred['title'], book['title']))
        return preds

    def check_needed(self, book, visited=set()):
        preds = []
        for pred in book['predecessors']:
            if pred != '':
                for predpred in self.books:
                    if predpred['title'] == pred:
                        self.check_needed(predpred)
                        if not predpred['selected']:
                            predpred['needed'] = True
                        preds.append((predpred['title'], book['title']))
        parallels_list = []
        visited.add(book['title'])
        for parallel_title in book['parallels']:
            if parallel_title != '' and parallel_title not in visited:
                for parallel_book in self.books:
                    if parallel_book['title'] == parallel_title:
                        visited.add(parallel_book['title'])
                        parallels_list.extend(self.check_needed(parallel_book, visited))
                        if (book['title'], parallel_book['title']) not in parallels_list and \
                        (parallel_book['title'], book['title']) not in parallels_list:
                            parallels_list.append((book['title'], parallel_book['title']))
        for a, b in parallels_list:
            for book in self.books:
                if book['title'] == a or book['title'] == b:
                    if not book['selected']:
                        book['needed'] = True    
        return parallels_list

    def get_full_parallels(self, book, visited=set()):
        parallels_list = []
        visited.add(book['title'])
        for parallel_title in book['parallels']:
            if parallel_title != '' and parallel_title not in visited:
                for parallel_book in self.books:
                    if parallel_book['title'] == parallel_title:
                        visited.add(parallel_book['title'])
                        parallels_list.extend(self.get_full_parallels(parallel_book, visited))
                        if (book['title'], parallel_book['title']) not in parallels_list and \
                        (parallel_book['title'], book['title']) not in parallels_list:
                            parallels_list.append((book['title'], parallel_book['title']))            
        return parallels_list



    def create_lists(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        updated_label = ttk.Label(self.root, text="Loading...")
        updated_label.grid(row=0, column=0, columnspan=12, padx=10, pady=10, sticky=tk.NSEW)

        finalbooks = []
        predecessors = []
        parallels = []
        pages = []

        initial_selected = [b['title'] for b in self.books if b['selected']]
        for book in self.books:
            if book['selected'] or book['needed']:
                finalbooks.append(book['title'])
                pages.append(book['pages'])
                self.check_needed(book)
                predecessors += self.get_full_predecessors(book)
                parallels += self.get_full_parallels(book)
        for book in self.books:
            if (book['selected'] or book['needed']) and book['title'] not in finalbooks:
                finalbooks.append(book['title'])
                pages.append(book['pages'])

        generator = BookGraphGenerator(num_books=0, level=3, random_seed=0, results=True, sequential_program=False,
                                    show_graph=True)
        generator.book_graph_from_selection(finalbooks, predecessors, parallels, pages, to_read=initial_selected)
        generator.write_pddl_file()
        timed = generator.run_metricff(60)
        r = generator.get_results()

        updated_label.config(text=r)

        month_labels = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER','NOVEMBER', 'DECEMBER']
        month_counts = {month: 1 for month in month_labels}
        book_assignments = r

        for widget in self.root.winfo_children():
            widget.destroy()

        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        for month in month_labels:
            book_label = ttk.Label(self.root, text=month, image="", compound=tk.TOP, background="bisque")
            book_label.config(font=('Helvetica bold', 10))
            book_label.grid(row=0, column=month_labels.index(month), padx=1, pady=1)

        if r != [] and r[0] != "This problem couldn't be solved in less than 60 seconds.":
            print(book_assignments)
            for book, month in book_assignments:
                label_text = f"{book}"
                image_path = ""
                for b in self.books:
                    if b['title'].upper().strip() in book:
                        image_path = b['image_url']

                try:
                    img = Image.open(image_path)
                except:
                    img = Image.open("./Media/Images/noimage.png")
                img = img.resize((80, 105), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)

                book_label = ttk.Label(self.root, text=label_text, image=photo, compound=tk.TOP, background="bisque")
                book_label.config(font=('Helvetica bold', 4))
                print(month_labels.index(month))
                book_label.grid(row=month_counts[month], column=month_labels.index(month), padx=1, pady=1)
                book_label.image = photo

                month_counts[month] += 1

        # Set weights for all rows and columns
        for row in range(max(month_counts.values()) + 2):
            self.root.grid_rowconfigure(row, weight=1)

        self.max = max(month_counts.values()) + 2

        self.root.grid_rowconfigure(self.max -1, weight=0)
        for col in range(1, 13):
            self.root.grid_columnconfigure(col, weight=1)

        back_button = ttk.Button(self.root, text="Back", command=self.create_interface)
        back_button.grid(row=max(month_counts.values()) + 1, column=0, columnspan=12, padx=10, pady=10, sticky=tk.NSEW)


        

if __name__ == "__main__":
    root = tk.Tk()
    app = BookSelectorApp(root, False)
    root.mainloop()

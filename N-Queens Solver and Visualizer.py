//Created by Aryan Gupta
import tkinter as tk
class NQueensSolverGUI:
    # Inner class representing the N-Queens solver
    class NQueensSolver:
        # Constructor to initialize the solver with the board size (n)
        def __init__(self, n):
            self.n = n  # Board size
            self.solutions = []  # List to store solutions

        # Method to solve the N-Queens problem and return solutions
        def solve(self):
            self.solutions = []  # Clear previous solutions
            self.backtrack(0, [])  # Start backtracking from the first row
            return self.solutions  # Return the list of solutions

        # Recursive backtracking method to find solutions
        def backtrack(self, row, solution):
            # Base case: If all queens are placed, add the solution to the list
            if row == self.n:
                self.solutions.append(solution[:])
                return

            # Try placing a queen in each column of the current row
            for col in range(self.n):
                # If it's safe to place a queen at the current position
                if self.is_safe(row, col, solution):
                    solution.append(col)  # Place the queen
                    self.backtrack(row + 1, solution)  # Recur for the next row
                    solution.pop()  # Backtrack: Remove the queen from the current position

        # Method to check if it's safe to place a queen at the given position
        def is_safe(self, row, col, solution):
            for r, c in enumerate(solution):
                # Check if there is a queen in the same column or diagonals
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

    # Constructor to initialize the GUI
    def __init__(self, root):
        self.root = root  # Tkinter root window
        self.root.title("N-Queens Solver")  # Set the title
        self.root.geometry("800x600")  # Set the initial window size
        # Variable to store the selected theme (Light or Dark)
        self.theme_var = tk.StringVar()
        self.theme_var.set("Light")  # Default theme is Light
        # Create and pack the theme selection label
        self.label_theme = tk.Label(self.root, text="Select Theme:", font=("Arial", 16))
        self.label_theme.pack(pady=10)
        # Create and pack the theme option menu
        self.option_menu = tk.OptionMenu(self.root, self.theme_var, "Light", "Dark", command=self.update_theme)
        self.option_menu.config(font=("Arial", 14))
        self.option_menu.pack(pady=5)
        # Create and pack the label to enter the value of N (board size)
        self.label = tk.Label(self.root, text="Enter the value of N:", font=("Arial", 24))
        self.label.pack(pady=20)
        # Create and pack the entry widget to input the value of N
        self.entry = tk.Entry(self.root, font=("Arial", 24))
        self.entry.pack(pady=10)
        # Create and pack the button to trigger the solving process
        self.solve_button = tk.Button(self.root, text="Solve", font=("Arial", 24), command=self.solve)
        self.solve_button.pack(pady=10)                   
        # Create and pack the text widget to display the solutions
        self.output_text = tk.Text(self.root, height=20, width=80, font=("Arial", 18))
        self.output_text.pack(pady=20)
        # Call the update_theme method to apply the initial theme settings

        self.update_theme()

    # Method to update the theme based on user selection
    def update_theme(self, *args):
        theme = self.theme_var.get()
        if theme == "Dark":
            # Dark theme settings
            self.root.config(bg="gray10")
            self.label_theme.config(bg="gray10", fg="white")
            self.label.config(bg="gray10", fg="white")
            self.entry.config(bg="gray20", fg="white")
            self.solve_button.config(bg="blue", fg="white")
            self.output_text.config(bg="gray20", fg="white")
        else:
            # Light theme settings
            self.root.config(bg="white")
            self.label_theme.config(bg="white", fg="black")
            self.label.config(bg="white", fg="black")
            self.entry.config(bg="lightgray", fg="black")
            self.solve_button.config(bg="blue", fg="white")
            self.output_text.config(bg="lightgray", fg="black")

    # Method to trigger the solving process
    def solve(self):
        # Clear previous output
        self.output_text.delete('1.0', tk.END)
        # Get the value of N from the entry widget
        n = int(self.entry.get())
        # Create an instance of the NQueensSolver with the specified board size
        solver = self.NQueensSolver(n)
        # Solve the N-Queens problem and get the solutions
        solutions = solver.solve()

        # Display the solutions in the output text widget
        if not solutions:
            self.output_text.insert(tk.END, f"There is no solution for the {n}-Queens problem.", "error")
        else:
            self.output_text.insert(tk.END, f"Found {len(solutions)} solution(s) for the {n}-Queens problem:\n\n")
            for i, solution in enumerate(solutions, 1):
                self.output_text.insert(tk.END, f"Solution {i}:\n")
                self.output_text.insert(tk.END, self.format_solution(solution), "solution")
                self.output_text.insert(tk.END, "\n\n")

    # Method to format the solution for display
    def format_solution(self, solution):
        formatted_solution = ""
        for row in solution:
            line = ['□'] * len(solution)
            line[row] = '♛'
            formatted_solution += ' '.join(line) + "\n"
        return formatted_solution.strip()

# Main block to create the root window and run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the Tkinter root window
    app = NQueensSolverGUI(root)  # Create an instance of the NQueensSolverGUI
    # Define text tag configurations for styling
    app.output_text.tag_configure("solution", foreground="green")
    app.output_text.tag_configure("error", foreground="red")
    root.mainloop()  # Run the Tkinter event loop //Created by Aryan Gupta


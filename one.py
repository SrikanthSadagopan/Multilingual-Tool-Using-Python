import tkinter as tk
from tkinter import ttk
from googletrans import Translator
import random

def get_translation(word, dest_language):
    translator = Translator()
    translation = translator.translate(word, dest=dest_language).text
    return translation

def compare_languages():
    word = entry_word_compare.get().strip().lower()
    lang1 = entry_lang1_compare.get().strip().lower()
    lang2 = entry_lang2_compare.get().strip().lower()

    supported_languages = ['en', 'hi', 'bn', 'te', 'mr', 'ta', 'ur', 'gu', 'kn', 'or',
                           'fr', 'de', 'es', 'it', 'nl', 'pt', 'ru', 'zh-cn', 'ja']

    languages = { "en": "English", "hi": "Hindi", "bn": "Bengali", "te": "Telugu","mr": "Marathi","ta": "Tamil","ur": "Urdu","gu": "Gujarati","kn": "Kannada",
    "or": "Odia","fr": "French","de": "German","es": "Spanish","it": "Italian","nl": "Dutch","pt": "Portuguese","ru": "Russian","zh-cn": "Chinese Simplified",
    "ja": "Japanese"
    }
    if lang1 not in supported_languages or lang2 not in supported_languages:
        result_label_compare.config(text="Unsupported language. Please choose from the supported languages.", fg="#ff6b6b")
        return

    translation1 = get_translation(word, lang1)
    translation2 = get_translation(word, lang2)

    result_label_compare.config(text=f"In {languages[lang1]} ({lang1.upper()}), '{word}' is called: {translation1}\n"
                                     f"In {languages[lang2]} ({lang2.upper()}), '{word}' is called: {translation2}", fg="#1d7a06")

def translate():
    word = entry_word_translate.get().strip().lower()
    dest_language = entry_lang_translate.get().strip().lower()

    supported_languages = ['en', 'hi', 'bn', 'te', 'mr', 'ta', 'ur', 'gu', 'kn', 'or',
                           'fr', 'de', 'es', 'it', 'nl', 'pt', 'ru', 'zh-cn', 'ja']

    languages = { "en": "English", "hi": "Hindi", "bn": "Bengali", "te": "Telugu","mr": "Marathi","ta": "Tamil","ur": "Urdu","gu": "Gujarati","kn": "Kannada",
    "or": "Odia","fr": "French","de": "German","es": "Spanish","it": "Italian","nl": "Dutch","pt": "Portuguese","ru": "Russian","zh-cn": "Chinese Simplified",
    "ja": "Japanese"
    }

    if dest_language not in supported_languages:
        result_label_translate.config(text="Unsupported language. Please choose from the supported languages.", fg="#ff6b6b")
        return

    translation = get_translation(word, dest_language)
    result_label_translate.config(text=f"The translation of '{word}' to {languages[dest_language]} ({dest_language.upper()}) is: {translation}", fg="#135403")

def french_vocabulary_quiz():
    # List of French words for the quiz
    vocabulary = {
        "apple": "pomme",
        "banana": "banane",
        "cat": "chat",
        "dog": "chien",
        "house": "maison",
        "car": "voiture",
        "book": "livre",
        "computer": "ordinateur",
        "friend": "ami",
        "school": "école"
    }

    # Initialize quiz variables, limit to 5 questions
    quiz_data = list(vocabulary.items())
    random.shuffle(quiz_data)
    quiz_data = quiz_data[:5]  # Take only the first 5 questions

    def start_practice_quiz():
        """Starts the practice quiz where answers are checked after each question."""
        total_questions = len(quiz_data)
        current_question = 0
        score = 0

        # Disable the buttons when the quiz starts
        practice_quiz_button.config(state=tk.DISABLED)
        quiz_button.config(state=tk.DISABLED)

        def show_question():
            """Displays the current question and resets the answer field."""
            word, _ = quiz_data[current_question]
            question_label.config(text=f"Question {current_question + 1}/{total_questions}: What is the French word for '{word}'?")
            answer_entry.delete(0, tk.END)
            feedback_label.config(text="")

        def check_answer():
            """Checks if the user's answer is correct and provides immediate feedback."""
            nonlocal current_question, score
            word, correct_translation = quiz_data[current_question]
            user_answer = answer_entry.get().strip().lower()

            if user_answer == correct_translation.lower():
                feedback_label.config(text="Correct!", fg="#de9bcf")
                score += 1
            else:
                feedback_label.config(text=f"Incorrect. The correct answer is '{correct_translation}'.", fg="#de9bcf")

            submit_button.config(state=tk.DISABLED)
            next_button.config(state=tk.NORMAL)

        def next_question():
            """Advances to the next question."""
            nonlocal current_question
            current_question += 1
            if current_question < total_questions:
                submit_button.config(state=tk.NORMAL)
                next_button.config(state=tk.DISABLED)
                show_question()
            else:
                show_summary()

        def show_summary():
            """Displays the final score summary at the end of the quiz."""
            question_label.config(text="Quiz Finished!")
            feedback_label.config(text=f"You scored {score} out of {total_questions}.", fg="#de9bcf")
            answer_entry.pack_forget()
            submit_button.pack_forget()
            next_button.pack_forget()

        # Set up the quiz interface
        show_question()

        # Buttons for Practice Quiz
        submit_button.config(command=check_answer, state=tk.NORMAL)
        next_button.config(command=next_question)

    def start_quiz():
        """Starts the quiz where answers are not revealed until the end."""
        total_questions = len(quiz_data)
        current_question = 0
        score = 0
        user_answers = []

        # Disable the buttons when the quiz starts
        practice_quiz_button.config(state=tk.DISABLED)
        quiz_button.config(state=tk.DISABLED)

        def show_question():
            """Displays the current question and resets the answer field."""
            word, _ = quiz_data[current_question]
            question_label.config(text=f"Question {current_question + 1}/{total_questions}: What is the French word for '{word}'?")
            answer_entry.delete(0, tk.END)
            feedback_label.config(text="")

        def submit_answer():
            """Records the user's answer and advances to the next question without feedback."""
            nonlocal current_question
            word, correct_translation = quiz_data[current_question]
            user_answer = answer_entry.get().strip().lower()

            # Store the user's answer and the correct answer
            user_answers.append((word, user_answer, correct_translation))
            current_question += 1

            if current_question < total_questions:
                show_question()
            else:
                show_summary()

        def show_summary():
            """Displays the summary of all answers and the final score."""
            question_label.config(text="Quiz Finished!")
            score = sum(1 for _, user_answer, correct_answer in user_answers if user_answer == correct_answer.lower())

            summary = "\n".join([f"Q: '{word}' -> Your answer: '{user_answer}', Correct answer: '{correct_answer}'"
                                 for word, user_answer, correct_answer in user_answers])

            feedback_label.config(text=f"Your score: {score}/{total_questions}\n\n{summary}", fg="#d4abcb")
            answer_entry.pack_forget()
            submit_button.pack_forget()

        # Set up the quiz interface
        show_question()

        # Buttons for Quiz
        submit_button.config(command=submit_answer, state=tk.NORMAL)
        next_button.pack_forget()  # No need for "Next" in this quiz format

    # Set up the quiz interface for both quizzes
    quiz_frame = tk.Frame(notebook, bg=tab_bg_color)
    notebook.add(quiz_frame, text="Quiz")

    instruction_label = tk.Label(quiz_frame, text="Choose the type of quiz:", bg=tab_bg_color, fg=tab_fg_color, font=label_font)
    instruction_label.pack(pady=(10, 10))

    question_label = tk.Label(quiz_frame, text="", bg=tab_bg_color, fg=tab_fg_color, font=label_font)
    question_label.pack(pady=(10, 10))

    answer_entry = tk.Entry(quiz_frame, width=entry_width, bg=tab_entry_bg, font=label_font)
    answer_entry.pack(pady=(10, 10))

    submit_button = tk.Button(quiz_frame, text="Submit Answer", font=button_font, bg="#6ab04c", fg="white", state=tk.DISABLED)
    submit_button.pack(pady=(10, 10))

    next_button = tk.Button(quiz_frame, text="Next Question", font=button_font, bg="#6ab04c", fg="white", state=tk.DISABLED)
    next_button.pack(pady=(10, 10))

    feedback_label = tk.Label(quiz_frame, text="", bg=tab_bg_color, fg="black", font=label_font)
    feedback_label.pack(pady=(10, 10))

    practice_quiz_button = tk.Button(quiz_frame, text="Practice Quiz", font=button_font, bg="#6ab04c", fg="white", command=start_practice_quiz)
    practice_quiz_button.pack(pady=(10, 10))

    quiz_button = tk.Button(quiz_frame, text="Quiz", font=button_font, bg="#6ab04c", fg="white", command=start_quiz)
    quiz_button.pack(pady=(10, 10))

def main():
    global root, entry_word_translate, entry_lang_translate, entry_word_compare, entry_lang1_compare, entry_lang2_compare
    global result_label_translate, result_label_compare, result_label_quiz, notebook
    global tab_bg_color, tab_fg_color, label_font, entry_width, button_font, result_font
    global tab_entry_bg

    root = tk.Tk()
    root.title("Multilingual Language Tool")
    root.geometry("600x600")
    root.configure(bg="#2c3e50")

    # Create Notebook (Tab Control)
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # Define a common style for entry fields (uniform size)
    entry_width = 40

    # Set up attractive backgrounds and colors for the tabs
    tab_bg_color = "#34495e"
    tab_fg_color = "#ecf0f1"
    tab_entry_bg = "#dff9fb"

    # Font styles
    header_font = ("Verdana", 16, "bold")
    label_font = ("Verdana", 12)
    result_font = ("Verdana", 11, "italic")
    button_font = ("Verdana", 10, "bold")

    # Supported languages
    supported_languages = """Supported Languages:
    English (en), Hindi (hi), Bengali (bn), Telugu (te),
    Marathi (mr), Tamil (ta), Urdu (ur), Gujarati (gu), 
    Kannada (kn), Odia (or), French (fr), German (de),
    Spanish (es), Italian (it), Dutch (nl), Portuguese (pt),
    Russian (ru), Chinese Simplified (zh-cn), Japanese (ja)
    """

    # Translation Tab
    translation_frame = tk.Frame(notebook, bg=tab_bg_color)
    notebook.add(translation_frame, text="Translation")

    label_translate = tk.Label(translation_frame, text="Translation", bg=tab_bg_color, fg=tab_fg_color, font=header_font)
    label_translate.pack(pady=(10, 10))

    label_supported_translate = tk.Label(translation_frame, text=supported_languages, bg=tab_bg_color, fg="#e8dae6", font=("Verdana", 10, "bold"))
    label_supported_translate.pack(pady=(0, 10))

    label_word_translate = tk.Label(translation_frame, text="Enter the English word:", bg=tab_bg_color, fg=tab_fg_color, font=label_font)
    label_word_translate.pack()
    entry_word_translate = tk.Entry(translation_frame, width=entry_width, bg=tab_entry_bg, font=label_font)
    entry_word_translate.pack()

    label_dest_lang_translate = tk.Label(translation_frame, text="Enter the destination language code:", bg=tab_bg_color, fg=tab_fg_color, font=label_font)
    label_dest_lang_translate.pack()
    entry_lang_translate = tk.Entry(translation_frame, width=entry_width, bg=tab_entry_bg, font=label_font)
    entry_lang_translate.pack()

    translate_button = tk.Button(translation_frame, text="Translate", command=translate, font=button_font, bg="#6ab04c", fg="white")
    translate_button.pack(pady=(10, 20))

    result_label_translate = tk.Label(translation_frame, text="...", bg="#fcfcfc", font=result_font)
    result_label_translate.pack()

    # Comparison Tab
    comparison_frame = tk.Frame(notebook, bg=tab_bg_color)
    notebook.add(comparison_frame, text="Language Comparison Tool")

    label_compare = tk.Label(comparison_frame, text="Language Comparison Tool", bg=tab_bg_color, fg=tab_fg_color, font=header_font)
    label_compare.pack(pady=(10, 10))

    label_supported_compare = tk.Label(comparison_frame, text=supported_languages, bg=tab_bg_color, fg="#e8dae6", font=("Verdana", 10, "bold"))
    label_supported_compare.pack(pady=(0, 10))

    label_word_compare = tk.Label(comparison_frame, text="Enter the English word:", bg=tab_bg_color, fg=tab_fg_color, font=label_font)
    label_word_compare.pack()
    entry_word_compare = tk.Entry(comparison_frame, width=entry_width, bg=tab_entry_bg, font=label_font)
    entry_word_compare.pack()

    label_lang1_compare = tk.Label(comparison_frame, text="Enter the first language code:", bg=tab_bg_color, fg=tab_fg_color, font=label_font)
    label_lang1_compare.pack()
    entry_lang1_compare = tk.Entry(comparison_frame, width=entry_width, bg=tab_entry_bg, font=label_font)
    entry_lang1_compare.pack()

    label_lang2_compare = tk.Label(comparison_frame, text="Enter the second language code:", bg=tab_bg_color, fg=tab_fg_color, font=label_font)
    label_lang2_compare.pack()
    entry_lang2_compare = tk.Entry(comparison_frame, width=entry_width, bg=tab_entry_bg, font=label_font)
    entry_lang2_compare.pack()

    compare_button = tk.Button(comparison_frame, text="Compare", command=compare_languages, font=button_font, bg="#6ab04c", fg="white")
    compare_button.pack(pady=(10, 20))

    result_label_compare = tk.Label(comparison_frame, text="...", bg="#fcfcfc", font=result_font)
    result_label_compare.pack()

    # Quiz Tab Button
    quiz_frame = tk.Frame(notebook, bg=tab_bg_color)
    notebook.add(quiz_frame, text="French Quiz")

    label_quiz = tk.Label(quiz_frame, text="French Vocabulary Quiz", bg=tab_bg_color, fg=tab_fg_color, font=header_font)
    label_quiz.pack(pady=(10, 10))

    quiz_button = tk.Button(quiz_frame, text="Select Quiz Type", command=french_vocabulary_quiz, font=button_font, bg="#6ab04c", fg="white")
    quiz_button.pack(pady=(10, 10))

    result_label_quiz = tk.Label(quiz_frame, text="", bg=tab_bg_color, fg=tab_fg_color, font=result_font)
    result_label_quiz.pack()

    button_exit = tk.Button(root, text="Exit", command=root.destroy, font=button_font, bg="#e74c3c", fg="white")
    button_exit.pack(pady=(20, 0))

    root.mainloop()

if __name__ == "__main__":
    main()

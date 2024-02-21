import tkinter as tk
import requests
# from googletrans import Translator, LANGUAGES
from google_trans_new import google_translator  
# translator = google_translator()  
from deep_translator import GoogleTranslator

'''
{'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}'''
# Initialize the variable
LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "zh-CN": "Chinese (Simplified)",
    "ar": "Arabic",
    "pt": "Portuguese",
    "ru": "Russian",
    "ja": "Japanese",
}

calculator_window = None
stopwatch_window = None
menu_bar = None
# TT = Translator()
print("translator initialized")

# # Define the LANGUAGES dictionary with language codes and names
# LANGUAGES = {
#     "en": "English",
#     "es": "Spanish",
#     "fr": "French",
#     "zh-cn": "Chinese (Simplified)",
#     "ar": "Arabic",
#     "pt": "Portuguese",
#     "ru": "Russian",
#     "ja": "Japanese",
# }
# Class to create a blueprint for creating stopwatch objects.

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        # Initialize the time elapsed and running status

        self.time_elapsed = 0
        self.running = False

        # Create label to display time and buttons for starting and resetting the stopwatch

        self.time_label = tk.Label(root, text="0:00.0", font=("Calibri", 36))
        self.start_button = tk.Button(root, text="Start", command=self.start_stop)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)

        # Put the labels and buttons in the GUI window

        self.time_label.pack(pady=20)
        self.start_button.pack()
        self.reset_button.pack()

        # Use the update_time method

        self.update_time()

    # Start and stop the stopwatch

    def start_stop(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
        else:
            self.running = True
            self.start_button.config(text="Stop")
            self.update_time()

    # Reset the stopwatch

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.time_label.config(text="0:00.0")
        self.start_button.config(text="Start")

    # Update the time for the stopwatch on the label

    def update_time(self):
        if self.running:
            self.time_elapsed += 0.1
            minutes = int(self.time_elapsed / 60)
            seconds = int(self.time_elapsed % 60)
            tenths = int((self.time_elapsed * 10) % 10)
            time_str = f"{minutes}:{seconds:02}.{tenths}"
            self.time_label.config(text=time_str)

            # Use the update_time method after 100 milliseconds

            self.root.after(100, self.update_time)

# Define open stopwatch command and window

def open_stopwatch():

    # Making the stopwatch window global to keep track of the window
    global stopwatch_window
    if stopwatch_window is not None:
        return
    stopwatch_window = tk.Toplevel(root)
    stopwatch_window.title("Stopwatch")

    stopwatch_window.geometry("270x200")

    stopwatch = Stopwatch(stopwatch_window)


# Exit Stopwatch

def exit_stopwatch():
    global stopwatch_window
    if stopwatch_window is not None:
        stopwatch_window.destroy()
        stopwatch_window = None

# Start a calculator def and add calculation methods

def open_calculator():
    global calculation
    calculation = ""

    # Add calculation for numbers and symbols

    def add_to_calculation(symbol):
        global calculation
        calculation += str(symbol)
        text_results.delete(1.0, "end")
        text_results.insert(1.0, calculation)

    # Evaluate calculation with all the added numbers and symbols

    def evaluate_calculation():

        global calculation
        try:
            # Evaluate calculation, and convert the result to string
            calculation = str(eval(calculation))
            text_results.delete(1.0, "end")
            text_results.insert(1.0, calculation)
        except Exception as e:
            clear_field()
            text_results.insert(1.0, "Error")

    # Clear calculation results

    def clear_field():
        global calculation
        calculation = ""
        text_results.delete(1.0, "end")

    # Create a new calculator window

    calculator = tk.Toplevel(root)
    calculator.title("Calculator")

    calculator.geometry("270x300")

    text_results = tk.Text(calculator, height=2, width=16, font=("Calibri", 24))
    text_results.grid(columnspan=5)

    # Make all the buttons in rows and columns for each individual functions adding to the calculation

    # Use lambda to pass arguments to the add_to_calculation function
    btn_1 = tk.Button(calculator, text="1", command=lambda: add_to_calculation(1), width=5, font=("calibri", 14))
    btn_1.grid(row=2, column=1)
    btn_2 = tk.Button(calculator, text="2", command=lambda: add_to_calculation(2), width=5, font=("calibri", 14))
    btn_2.grid(row=2, column=2)
    btn_3 = tk.Button(calculator, text="3", command=lambda: add_to_calculation(3), width=5, font=("calibri", 14))
    btn_3.grid(row=2, column=3)
    btn_4 = tk.Button(calculator, text="4", command=lambda: add_to_calculation(4), width=5, font=("calibri", 14))
    btn_4.grid(row=3, column=1)
    btn_5 = tk.Button(calculator, text="5", command=lambda: add_to_calculation(5), width=5, font=("calibri", 14))
    btn_5.grid(row=3, column=2)
    btn_6 = tk.Button(calculator, text="6", command=lambda: add_to_calculation(6), width=5, font=("calibri", 14))
    btn_6.grid(row=3, column=3)
    btn_7 = tk.Button(calculator, text="7", command=lambda: add_to_calculation(7), width=5, font=("calibri", 14))
    btn_7.grid(row=4, column=1)
    btn_8 = tk.Button(calculator, text="8", command=lambda: add_to_calculation(8), width=5, font=("calibri", 14))
    btn_8.grid(row=4, column=2)
    btn_9 = tk.Button(calculator, text="9", command=lambda: add_to_calculation(9), width=5, font=("calibri", 14))
    btn_9.grid(row=4, column=3)
    btn_0 = tk.Button(calculator, text="0", command=lambda: add_to_calculation(0), width=5, font=("calibri", 14))
    btn_0.grid(row=5, column=2)

    btn_plus = tk.Button(calculator, text="+", command=lambda: add_to_calculation("+"), width=5, font=("calibri", 14))
    btn_plus.grid(row=2, column=4)
    btn_minus = tk.Button(calculator, text="-", command=lambda: add_to_calculation("-"), width=5, font=("calibri", 14))
    btn_minus.grid(row=3, column=4)
    btn_times = tk.Button(calculator, text="*", command=lambda: add_to_calculation("*"), width=5, font=("calibri", 14))
    btn_times.grid(row=4, column=4)
    btn_divide = tk.Button(calculator, text="/", command=lambda: add_to_calculation("/"), width=5, font=("calibri", 14))
    btn_divide.grid(row=5, column=4)

    btn_open = tk.Button(calculator, text="(", command=lambda: add_to_calculation("("), width=5, font=("calibri", 14))
    btn_open.grid(row=5, column=1)
    btn_close = tk.Button(calculator, text=")", command=lambda: add_to_calculation(")"), width=5, font=("calibri", 14))
    btn_close.grid(row=5, column=3)

    btn_equals = tk.Button(calculator, text="=", command=evaluate_calculation, width=11, font=("calibri", 14))
    btn_equals.grid(row=6, column=3, columnspan=2)
    btn_clear = tk.Button(calculator, text="C", command=clear_field, width=11, font=("calibri", 14))
    btn_clear.grid(row=6, column=1, columnspan=2)

# Exit calculator

def exit_calculator():
    calculator_window.destroy()

# Start a new tip calculator

def tip_calc_window():
    tip_window = tk.Toplevel(root)
    tip_window.title("Tip Calculator")
    tip_window.geometry("300x300")

    label_tip_percent = tk.Label(tip_window, text="Enter Tip Percentage (%)")
    label_tip_percent.pack()

    entry_tip_percent = tk.Entry(tip_window)
    entry_tip_percent.pack()

    label_bill_dollars = tk.Label(tip_window, text="Enter the Bill Amount ($)")
    label_bill_dollars.pack()

    entry_bill_dollars = tk.Entry(tip_window)
    entry_bill_dollars.pack()

    # Calculate tip function

    def calculate_tip():
        try:
            tip_percent = float(entry_tip_percent.get())
            bill_dollars = float(entry_bill_dollars.get())
            tip_amount = tip_percent * bill_dollars / 100
            result_label.config(text=f'Your tip should be ${tip_amount}')
            result_label_total.config(text=f'Your total bill would be ${tip_amount + bill_dollars}')
        except ValueError:
            result_label.config(text="Please enter valid numbers.")
            result_label_total.config(text="")

    button_calculate = tk.Button(tip_window, text="Calculate", command=calculate_tip)
    button_calculate.pack()

    result_label = tk.Label(tip_window, text="", font=("Calibri", 12))
    result_label.pack()

    result_label_total = tk.Label(tip_window, text="", font=("Calibri", 12))
    result_label_total.pack()

# Start a todo list

def open_todo_list():
    todo_window = tk.Toplevel(root)
    todo_window.title("To-Do List")
    todo_window.geometry("300x400")

    tasks = []

    # Add task to the todo list

    def add_task():
        task = entry_task.get()
        if task:
            tasks.append(task)
            update_listbox()
            entry_task.delete(0,'end')

    # Remove task from the todo list

    def remove_task():
        selected_task = list_tasks.curselection()
        if selected_task:
            index = selected_task[0]
            del tasks[index]
            update_listbox()

    # Ranks each task from being added early to late

    def update_listbox():
        list_tasks.delete(0, tk.END)
        for task in tasks:
            list_tasks.insert(tk.END, task)

    label_task = tk.Label(todo_window, text="Task:")
    label_task.pack()

    entry_task = tk.Entry(todo_window, width=30)
    entry_task.pack()

    button_add_task = tk.Button(todo_window, text="Add Task", command=add_task)
    button_add_task.pack(pady=5)

    list_tasks = tk.Listbox(todo_window, width=30)
    list_tasks.pack()

    button_remove_task = tk.Button(todo_window, text="Remove Task", command=remove_task)
    button_remove_task.pack(pady=5)

    update_listbox()


# Creating the unit converter window
def add_todo_list_to_menu(menu_bar):
    todo_menu = tk.Menu(menu_bar, tearoff=0)
    todo_menu.add_command(label="Open", command=open_todo_list)
    menu_bar.add_cascade(label="To-Do List", menu=todo_menu)


def open_unit_convertor():

    unit_convertor_window = tk.Toplevel(root)
    unit_convertor_window.title("Unit Convertor")
    unit_convertor_window.geometry("500x400")

    # Converting Length Units
    def convert_length(direction):
        try:
            input_value = float(entry_length.get())
            if direction == "to_cm":
                converted_value = round(input_value * 2.54, 1)
                result_label_length.config(text=f'{input_value} inches is {converted_value} centimeters.')
            elif direction == "to_inches":
                converted_value = round(input_value / 2.54, 1)
                result_label_length.config(text=f'{input_value} centimeters is {converted_value} inches.')
        except ValueError:
            result_label_length.config(text="Please enter a valid number.")

    def convert_weight(direction):
        try:
            input_value = float(entry_weight.get())
            if direction == "to_kg":
                converted_value = round(input_value * 0.453592, 1)
                result_label_weight.config(text=f'{input_value} pounds is {converted_value} kilograms.')
            elif direction == "to_pounds":
                converted_value = round(input_value / 0.453592, 1)
                result_label_weight.config(text=f'{input_value} kilograms is {converted_value} pounds.')
        except ValueError:
            result_label_weight.config(text="Please enter a valid number.")

    def convert_temp(direction):
        try:
            input_value = float(entry_temp.get())
            if direction == "to_celsius":
                converted_value = round((input_value - 32) * 5 / 9, 1)
                result_label_temp.config(text=f'{input_value} Fahrenheit is {converted_value} Celsius.')
            elif direction == "to_fahrenheit":
                converted_value = round((input_value * 9 / 5) + 32, 1)
                result_label_temp.config(text=f'{input_value} Celsius is {converted_value} Fahrenheit.')
        except ValueError:
            result_label_temp.config(text="Please enter a valid number.")

        # Length Conversion

    label_length = tk.Label(unit_convertor_window, text="Convert Length:")
    label_length.pack()
    entry_length = tk.Entry(unit_convertor_window)
    entry_length.pack()
    button_to_cm = tk.Button(unit_convertor_window, text="To Centimeters", command=lambda: convert_length("to_cm"))
    button_to_cm.pack()
    button_to_inches = tk.Button(unit_convertor_window, text="To Inches", command=lambda: convert_length("to_inches"))
    button_to_inches.pack()
    result_label_length = tk.Label(unit_convertor_window, text="", font=("Calibri", 12))
    result_label_length.pack()

    # Weight Conversion
    label_weight = tk.Label(unit_convertor_window, text="Convert Weight:")
    label_weight.pack()
    entry_weight = tk.Entry(unit_convertor_window)
    entry_weight.pack()
    button_to_kg = tk.Button(unit_convertor_window, text="To Kilograms", command=lambda: convert_weight("to_kg"))
    button_to_kg.pack()
    button_to_pounds = tk.Button(unit_convertor_window, text="To Pounds", command=lambda: convert_weight("to_pounds"))
    button_to_pounds.pack()
    result_label_weight = tk.Label(unit_convertor_window, text="", font=("Calibri", 12))
    result_label_weight.pack()

    # Temperature Conversion
    label_temp = tk.Label(unit_convertor_window, text="Convert Temperature:")
    label_temp.pack()
    entry_temp = tk.Entry(unit_convertor_window)
    entry_temp.pack()
    button_to_celsius = tk.Button(unit_convertor_window, text="To Celsius", command=lambda: convert_temp("to_celsius"))
    button_to_celsius.pack()
    button_to_fahrenheit = tk.Button(unit_convertor_window, text="To Fahrenheit", command=lambda: convert_temp("to_fahrenheit"))
    button_to_fahrenheit.pack()
    result_label_temp = tk.Label(unit_convertor_window, text="", font=("Calibri", 12))
    result_label_temp.pack()

# Start the currency convertor

def open_currency_convertor():
    print("Open currency convertor called.\n")
    def convert_currency():
        try:
            amount = float(entry_amount.get())
            from_currency = combo_from_currency.get()
            to_currency = combo_to_currency.get()

            # API Request

            base_url = "https://open.er-api.com/v6/latest"
            params = {"apikey": currency_api_key, "base": from_currency}
            response = requests.get(base_url, params=params)
            data = response.json()

            # Calculate the converted amount
            conversion_rate = data["rates"][to_currency]
            converted_amount = round(amount * conversion_rate, 2)

            result_label_currency.config(text=f"{amount} {from_currency} is {converted_amount} {to_currency}")

        except ValueError:
            result_label_currency.config(text="Please enter a valid number.")
        except Exception as e:
            result_label_currency.config(text="Error fetching exchange rates.")

    currency_convertor_window = tk.Toplevel(root)
    currency_convertor_window.title("Currency Convertor")
    currency_convertor_window.geometry("300x200")

    label_amount = tk.Label(currency_convertor_window, text="Amount:")
    label_amount.pack()

    entry_amount = tk.Entry(currency_convertor_window)
    entry_amount.pack()

    label_from_currency = tk.Label(currency_convertor_window, text="From Currency:")
    label_from_currency.pack()

    combo_from_currency = tk.Entry(currency_convertor_window)
    combo_from_currency.pack()

    label_to_currency = tk.Label(currency_convertor_window, text="To Currency:")
    label_to_currency.pack()

    combo_to_currency = tk.Entry(currency_convertor_window)
    combo_to_currency.pack()

    button_convert_currency = tk.Button(currency_convertor_window, text="Convert", command=convert_currency)
    button_convert_currency.pack(pady=5)

    result_label_currency = tk.Label(currency_convertor_window, text="", font=("Calibri", 12))
    result_label_currency.pack()


# Start the Weather APP

def get_weather(weather_api_key, city):
    print("get weather called.\n")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature_celsius = round(data["main"]["temp"], 0)
            temperature_fahrenheit = round(temperature_celsius * 9/5 + 32, 0)
            description = data["weather"][0]["description"]
            return f"Temperature in {city} : {temperature_celsius}°C/{temperature_fahrenheit}°F. Weather: {description}"
        else:
            return f"Error: {data['message']}"

    except Exception as e:
        return f"Error: {str(e)}"


def fetch_weather(city_entry, state_entry, weather_label):
    print("fetch weather called.\n")
    global api_key
    user_city = city_entry.get()
    user_state = state_entry.get()

    if user_city:
        if user_state:
            city_and_state = f"{user_city},{user_state}"
        else:
            city_and_state = user_city

        weather_info = get_weather(weather_api_key, city_and_state)
        weather_label.config(text=weather_info)


def open_weather():
    print("Open weather called.\n")
    weather_window = tk.Toplevel(root)
    weather_window.title("Weather Information")
    weather_window.geometry("600x200")

    city_entry_label = tk.Label(weather_window, text="Enter City:")
    city_entry_label.pack()

    city_entry = tk.Entry(weather_window)
    city_entry.pack()

    state_entry_label = tk.Label(weather_window, text="Enter State (optional):")
    state_entry_label.pack()

    state_entry = tk.Entry(weather_window)
    state_entry.pack()

    weather_label = tk.Label(weather_window, text="", font=("Calibri", 12))
    weather_label.pack()

    fetch_button = tk.Button(weather_window, text="Get Weather", command=lambda: fetch_weather(city_entry, state_entry, weather_label))
    fetch_button.pack()

# Start the Translator App
# def open_translator():
#     print("Open_Translator called.\n")
#     translator_window = tk.Toplevel(root)
#     translator_window.title("Translator")
#     translator_window.geometry("400x400")

#     # Create input and output text widgets
#     input_text = tk.Text(translator_window, height=5, width=40, font=("Calibri", 12))
#     output_text = tk.Text(translator_window, height=5, width=40, font=("Calibri", 12), state="disabled")

#     input_text.pack(pady=10)
#     output_text.pack(pady=10)
#     print("input output packed.\n")
#     # Create language selection menus
#     source_language_label = tk.Label(translator_window, text="Select Source Language:")
#     source_language_label.pack()
#     source_language_var = tk.StringVar()
#     source_language_menu = tk.OptionMenu(translator_window, source_language_var, *LANGUAGES.values())
#     source_language_menu.pack()

#     target_language_label = tk.Label(translator_window, text="Select Target Language:")
#     target_language_label.pack()
#     target_language_var = tk.StringVar()
#     target_language_menu = tk.OptionMenu(translator_window, target_language_var, *LANGUAGES.values())
#     target_language_menu.pack()

#     # Create translation function
#     def translate_text():
#         print("started translate")
#         try:
#             text_to_translate = input_text.get("1.0", "end-1c").strip()

#             if not text_to_translate:
#                 return

#             # Get selected source and target languages
#             source_language = source_language_var.get()
#             target_language = target_language_var.get()

#             # Translate text to the selected target language
#             translation = translator.translate(text_to_translate, src=source_language, dest=target_language)
#             output_text.config(state="normal")
#             output_text.delete("1.0", "end")
#             output_text.insert("1.0", translation.text)
#             output_text.config(state="disabled")

#         except Exception as e:
#             output_text.delete("1.0", "end")
#             output_text.insert("1.0", f"Translation Error: {str(e)}")

#     translate_button = tk.Button(translator_window, text="Translate", command=translate_text)
#     translate_button.pack()

def open_translator():
    # TT = Translator(service_urls=['translate.googleapis.com'])
    print("Open_Translator called.\n")
    translator_window = tk.Toplevel(root)
    translator_window.title("Translator")
    translator_window.geometry("400x400")

    # Create input and output text widgets
    input_text = tk.Text(translator_window, height=5, width=40, font=("Calibri", 12))
    output_text = tk.Text(translator_window, height=5, width=40, font=("Calibri", 12), state="disabled")

    input_text.pack(pady=10)
    output_text.pack(pady=10)
    print("input output packed.\n")
    # Create language selection menus
    source_language_label = tk.Label(translator_window, text="Select Source Language:")
    source_language_label.pack()
    source_language_var = tk.StringVar()
    source_language_menu = tk.OptionMenu(translator_window, source_language_var, *LANGUAGES.values())
    source_language_menu.pack()

    target_language_label = tk.Label(translator_window, text="Select Target Language:")
    target_language_label.pack()
    target_language_var = tk.StringVar()
    target_language_menu = tk.OptionMenu(translator_window, target_language_var, *LANGUAGES.values())
    target_language_menu.pack()
    def languagecode(language_name):
        for code, name in LANGUAGES.items():
            if name.lower() == language_name.lower():
                return code
        return f"Error: Language '{language_name}' not found."
    # Create translation function
    def translate_text():
        print("started translate")
        try:
            text_to_translate = input_text.get("1.0", "end-1c").strip()
            print("checkpoint1")
            if not text_to_translate:
                print("here?")
                return

            # Get selected source and target languages
            print("checkpoint2")
            source_language = source_language_var.get()
            target_language = target_language_var.get()
            
            print(source_language)
            print(target_language)
            srcl = languagecode(source_language)
            destl = languagecode(target_language)
            # Translate text to the selected target language
            print(type(text_to_translate))
            print("texttotranslate " + text_to_translate)
            print(type(srcl))
            print("srcl :" + srcl)
            print(type(destl))
            print("destl :" + destl)
            translated = GoogleTranslator(source='en', target='zh-CN').translate('mother')
            print(translated)
            # try:
            #     translated_text = translator.translate('mother', lang_src='en', lang_tgt='fr')
            #     print(translated_text)
            # except Exception as e:
            #     print("An error occurred:", e)
            translation = GoogleTranslator(source=srcl,target=destl).translate(text_to_translate)
            print("here?")
            print("translation: " + translation)
            output_text.config(state="normal")
            output_text.delete("1.0", "end")
            output_text.insert("1.0", translation)
            output_text.config(state="disabled")

        except Exception as e:
            output_text.delete("1.0", "end")
            output_text.insert("1.0", f"Translation Error: {str(e)}")

    translate_button = tk.Button(translator_window, text="Translate", command=translate_text)
    translate_button.pack()

    # Add a print statement to indicate the end of the function
    print("open_translator function completed.")

# Start the Basic GUI window
print("Initializing application...")

root = tk.Tk()

root.title("USEFUL Toolbox")
root.geometry("600x600")

# api keys
currency_api_key = "a1361d0598a346dca2e06e97ba9aec3f"
weather_api_key = "fbdd760a4dbee3b2c84ed5ec8ca943c8"

# Create Menubar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add a dropdown menu for the Calculator
calculator_menu = tk.Menu(menu_bar, tearoff=0)
calculator_menu.add_command(label="Calculator", command=open_calculator)
calculator_menu.add_command(label="Tip Calculator", command=tip_calc_window)
calculator_menu.add_command(label="Exit", command=exit_calculator)

menu_bar.add_cascade(label="Calculators", menu=calculator_menu)

# Add a dropdown menu for the Stopwatch
stopwatch_menu = tk.Menu(menu_bar, tearoff=0)
stopwatch_menu.add_command(label="Open", command=open_stopwatch)
stopwatch_menu.add_command(label="Exit", command=exit_stopwatch)

menu_bar.add_cascade(label="Stopwatch", menu=stopwatch_menu)

root.config(menu=menu_bar)
print("Creating welcome label...")
# Create label for the welcoming message
welcome_label = tk.Label(root, text="Welcome to USEFUL Toolbox", font=("Calibri", 20), fg="#008B8B", bg="#FFD580")
print("Packing welcome label...")
welcome_label.pack(fill="both", expand=True)

# Add todo list to the menu as a dropdown menu
add_todo_list_to_menu(menu_bar)

# Add a dropdown menu for the Unit Converter
unit_convertor_menu = tk.Menu(menu_bar, tearoff=0)
unit_convertor_menu.add_command(label="Unit Convertor", command=open_unit_convertor)
menu_bar.add_cascade(label="Unit Convertor", menu=unit_convertor_menu)

# Add a dropdown menu for the Currency Convertor
currency_convertor_menu = tk.Menu(menu_bar, tearoff=0)
currency_convertor_menu.add_command(label="Currency Convertor", command=open_currency_convertor)
menu_bar.add_cascade(label="Currency Convertor", menu=currency_convertor_menu)

# Add a dropdown menu for Weather
weather_menu = tk.Menu(menu_bar, tearoff=0)
weather_menu.add_command(label="Weather Information", command=open_weather)
menu_bar.add_cascade(label="Weather", menu=weather_menu)

# Add a dropdown menu for the Translator
translator_menu = tk.Menu(menu_bar, tearoff=0)
translator_menu.add_command(label="Translator", command=open_translator)
menu_bar.add_cascade(label="Translator", menu=translator_menu)



root.mainloop()
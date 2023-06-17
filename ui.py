import tkinter
import customtkinter
from main import convertir

dictMonedas = {'AED': 'United Arab Emirates dirham',
                'AFN': 'Afghan afghani',
                'ALL': 'Albanian lek',
                'AMD': 'Armenian dram',
                'ANG': 'Netherlands Antillean guilder',
                'AOA': 'Angolan kwanza',
                'ARS': 'Argentine peso',
                'AUD': 'Australian dollar',
                'AWG': 'Aruban florin',
                'AZN': 'Azerbaijani manat',
                'BAM': 'Bosnia and Herzegovina convertible mark',
                'BBD': 'Barbadian dollar',
                'BDT': 'Bangladeshi taka',
                'BGN': 'Bulgarian lev',
                'BHD': 'Bahraini dinar',
                'BIF': 'Burundian franc',
                'BMD': 'Bermudian dollar',
                'BND': 'Brunei dollar',
                'BOB': 'Bolivian boliviano',
                'BRL': 'Brazilian real',
                'BSD': 'Bahamian dollar',
                'BTN': 'Bhutanese ngultrum',
                'BWP': 'Botswana pula',
                'BYN': 'Belarusian ruble',
                'BZD': 'Belize dollar',
                'CAD': 'Canadian dollar',
                'CDF': 'Congolese franc',
                'CHF': 'Swiss franc',
                'CLP': 'Chilean peso',
                'CNY': 'Renminbi',
                'COP': 'Colombian peso',
                'CRC': 'Costa Rican colón',
                'CUC': 'Cuban convertible peso',
                'CUP': 'Cuban peso',
                'CVE': 'Cape Verdean escudo',
                'CZK': 'Czech koruna',
                'DJF': 'Djiboutian franc',
                'DKK': 'Danish krone',
                'DOP': 'Dominican peso',
                'DZD': 'Algerian dinar',
                'EGP': 'Egyptian pound',
                'ERN': 'Eritrean nakfa',
                'ETB': 'Ethiopian birr',
                'EUR': 'Euro',
                'FJD': 'Fijian dollar',
                'FKP': 'Falkland Islands pound',
                'GBP': 'Pound sterling',
                'GEL': 'Georgian lari',
                'GGP': 'Guernsey pound',
                'GHS': 'Ghanaian cedi',
                'GIP': 'Gibraltar pound',
                'GMD': 'Gambian dalasi',
                'GNF': 'Guinean franc',
                'GTQ': 'Guatemalan quetzal',
                'GYD': 'Guyanese dollar',
                'HKD': 'Hong Kong dollar',
                'HNL': 'Honduran lempira',
                'HRK': 'Croatian kuna',
                'HTG': 'Haitian gourde',
                'HUF': 'Hungarian forint',
                'IDR': 'Indonesian rupiah',
                'ILS': 'Israeli new shekel',
                'IMP': 'Manx pound',
                'INR': 'Indian rupee',
                'IQD': 'Iraqi dinar',
                'IRR': 'Iranian rial',
                'ISK': 'Icelandic króna',
                'JEP': 'Jersey pound',
                'JMD': 'Jamaican dollar',
                'JOD': 'Jordanian dinar',
                'JPY': 'Japanese yen',
                'KES': 'Kenyan shilling',
                'KGS': 'Kyrgyzstani som',
                'KHR': 'Cambodian riel',
                'KMF': 'Comorian franc',
                'KRW': 'South Korean won',
                'KWD': 'Kuwaiti dinar',
                'KYD': 'Cayman Islands dollar',
                'KZT': 'Kazakhstani tenge',
                'LAK': 'Lao kip',
                'LBP': 'Lebanese pound',
                'LKR': 'Sri Lankan rupee',
                'LRD': 'Liberian dollar',
                'LSL': 'Lesotho loti',
                'LYD': 'Libyan dinar',
                'MAD': 'Moroccan dirham',
                'MDL': 'Moldovan leu',
                'MGA': 'Malagasy ariary',
                'MKD': 'Macedonian denar',
                'MMK': 'Burmese kyat',
                'MNT': 'Mongolian tögrög',
                'MOP': 'Macanese pataca',
                'MRU': 'Mauritanian ouguiya',
                'MUR': 'Mauritian rupee',
                'MVR': 'Maldivian rufiyaa',
                'MWK': 'Malawian kwacha',
                'MXN': 'Mexican peso',
                'MYR': 'Malaysian ringgit',
                'MZN': 'Mozambican metical',
                'NAD': 'Namibian dollar',
                'NGN': 'Nigerian naira',
                'NIO': 'Nicaraguan córdoba',
                'NOK': 'Norwegian krone',
                'NPR': 'Nepalese rupee',
                'NZD': 'New Zealand dollar',
                'OMR': 'Omani rial',
                'PAB': 'Panamanian balboa',
                'PEN': 'Peruvian sol',
                'PGK': 'Papua New Guinean kina',
                'PHP': 'Philippine peso',
                'PKR': 'Pakistani rupee',
                'PLN': 'Polish złoty',
                'PYG': 'Paraguayan guaraní',
                'QAR': 'Qatari riyal',
                'RON': 'Romanian leu',
                'RSD': 'Serbian dinar',
                'RUB': 'Russian ruble',
                'RWF': 'Rwandan franc',
                'SAR': 'Saudi riyal',
                'SBD': 'Solomon Islands dollar',
                'SCR': 'Seychellois rupee',
                'SDG': 'Sudanese pound',
                'SEK': 'Swedish krona',
                'SGD': 'Singapore dollar',
                'SHP': 'Saint Helena pound',
                'SLL': 'Sierra Leonean leone',
                'SOS': 'Somali shilling',
                'SRD': 'Surinamese dollar',
                'SSP': 'South Sudanese pound',
                'STN': 'São Tomé and Príncipe dobra',
                'SVC': 'Salvadoran colón',
                'SYP': 'Syrian pound',
                'SZL': 'Swazi lilangeni',
                'THB': 'Thai baht',
                'TJS': 'Tajikistani somoni',
                'TMT': 'Turkmenistan manat',
                'TND': 'Tunisian dinar',
                'TOP': 'Tongan paʻanga',
                'TRY': 'Turkish lira',
                'TTD': 'Trinidad and Tobago dollar',
                'TWD': 'New Taiwan dollar',
                'TZS': 'Tanzanian shilling',
                'UAH': 'Ukrainian hryvnia',
                'UGX': 'Ugandan shilling',
                'USD': 'United States dollar',
                'UYU': 'Uruguayan peso',
                'UZS': 'Uzbekistani soʻm',
                'VES': 'Venezuelan bolívar',
                'VND': 'Vietnamese đồng',
                'VUV': 'Vanuatu vatu',
                'WST': 'Samoan tālā',
                'XAF': 'Central African CFA franc',
                'XAG': 'Silver (troy ounce)',
                'XAU': 'Gold (troy ounce)',
                'XCD': 'Eastern Caribbean dollar',
                'XDR': 'Special drawing rights',
                'XOF': 'West African CFA franc',
                'XPF': 'CFP franc',
                'YER': 'Yemeni rial',
                'ZAR': 'South African rand',
                'ZMW': 'Zambian kwacha',
                'ZWL': 'Zimbabwean dollar'}
listaMonedas = []
for clave in dictMonedas:
     listaMonedas.append(clave)
#print(listaMonedas)
# TEMA--------------------------------------------------------
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green
# VENTANA-----------------------------------------------------
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x260")
app.title('Conversor')
app.iconbitmap('tipo-de-cambio.ico')
app.resizable(0,0)
# FRAME-----------------------------------------------
frame1 = customtkinter.CTkFrame(master=app, width=200, height=500,fg_color='#1f1f1f')
frame1.grid(row=0, column=0, padx=0, pady=0)
# FUNCIONES----------------------------------------------------------
def button_function():
    print("button pressed")
# LABEL-----------------------------------------------
text_var = tkinter.StringVar(value="Importe")
label = customtkinter.CTkLabel(master=frame1,
                               textvariable=text_var,
                               width=120,
                               height=25,
                               fg_color=("transparent"),
                               corner_radius=8)
label.place(relx=0.2, rely=0.19)
# TEXTBOX---------------------------------------------
textbox1 = customtkinter.CTkTextbox(master=app, width=200,height=150, corner_radius=4)
textbox1.place(relx=0.5, rely=0.2)

textbox1.insert("0.0", "Sample\n" * 5)
# BOTONES---------------------------------------------
button = customtkinter.CTkButton(master=app, text="Convertir", command=button_function)
button.place(relx=0.2, rely=0.7, anchor=tkinter.CENTER)
# ENTRADA-----------------------------------------
entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="$",
                               width=75,
                               height=25,
                               border_width=2,
                               corner_radius=5)
entry.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
# COMBOBOX -----------------------------
def combobox_callback(choice):
    print("moneda1:", choice)
combobox1 = customtkinter.CTkComboBox(app, values=listaMonedas,
                                     command=combobox_callback)
#combobox1.pack(padx=20, pady=10)
combobox1.place(relx=0.2, rely=0.1, anchor=tkinter.CENTER)
combobox1.set("USD")
#--------------------------------------------
def combobox_callback(choice):
    print("moneda2:", choice)
combobox2 = customtkinter.CTkComboBox(app, values=listaMonedas,
                                     command=combobox_callback)
#combobox2.pack(padx=20, pady=10)
combobox2.place(relx=0.2, rely=0.25, anchor=tkinter.CENTER)
combobox2.set("JPY")
#--------------------------------------------------
app.mainloop()
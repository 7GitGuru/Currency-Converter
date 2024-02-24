This currency converter project consists of a backend and frontend structure, utilizing Python and Flask for the backend logic, and HTML/CSS/JavaScript for the frontend components.

### Backend:
- **Flask Framework:** Used for routing, handling HTTP requests, and serving HTML templates.
- **SQLite Database:** Stores conversion history.

### Frontend:
- **HTML:** Structure and content of web pages.
- **CSS:** Stylesheets for styling the pages.
- **JavaScript:** Enables interactivity and handling of user actions.

### API Integration:
The project fetches real-time exchange rates from an external API service, such as exchangeratesapi.io. To integrate the API, you need to sign up on their website to obtain an API token or key. 

### Themes:
The project offers the choice between light and dark themes by connecting different stylesheet files: [`styles-dark.css`](https://github.com/7GitGuru/Currency-Converter/blob/main/static/css/styles-dark.css) for the dark theme and [`styles-white.css`](https://github.com/7GitGuru/Currency-Converter/blob/main/static/css/styles-white.css) for the light theme. 

To access real-time exchange rates, the project interacts with the chosen [API](https://exchangeratesapi.io/documentation/) by sending HTTP requests with the currencies to convert between and receiving responses containing the current exchange rates. The retrieved data is then processed and displayed to the user.

Overall, this currency converter project showcases the integration of backend logic with Flask, frontend design using HTML/CSS/JavaScript, and the utilization of an external API to retrieve real-time exchange rates, providing users with a practical tool for currency conversion.

---

### preview
<details>
  <summary><b>⬛Dark Theme</b></summary>
  
![image](https://github.com/7GitGuru/Currency-Converter/assets/154711952/15be8471-f2e7-4a7c-80a6-c96dfc4e3883)
![image](https://github.com/7GitGuru/Currency-Converter/assets/154711952/cb17953b-a075-46d2-8b1e-e23c8cb30051)
![image](https://github.com/7GitGuru/Currency-Converter/assets/154711952/cfa88924-c4f2-4e70-bba9-15d1be7c08cd)
![image](https://github.com/7GitGuru/Currency-Converter/assets/154711952/752dbb71-9a5f-4f1e-9c31-3ccde8a62a08)

</details>

<details>
  <summary><b>⬜White Theme</b></summary>
  
![image](https://github.com/7GitGuru/Currency-Converter/assets/154711952/0a81ea7c-c9d6-4820-ad16-ce5cb7b34905)
![image](https://github.com/7GitGuru/Currency-Converter/assets/154711952/0a2e0510-8284-48d2-8b1b-ee4bbba7c2c9)
![image](https://github.com/7GitGuru/Currency-Converter/assets/154711952/279d9e3b-8363-48cf-a4f4-e0be68aaf48a)

</details>








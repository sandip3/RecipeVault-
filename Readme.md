# **RecipeVault: A Django-Powered Food Recipe App**

---

## **Overview**
- **RecipeVault** is a food recipe management app developed using:
  - **Django** (Backend)
  - **HTML**, **CSS**, and **Bootstrap** (Frontend)
- Features include:
  - **Create**, **View**, **Update**, **Delete**, and **Search** recipes.
  - Allows users to upload images for each recipe.
  - Provides a responsive design for mobile and desktop.

---

## **Technologies Used**
- **Frontend**:
  - **HTML**: Structure and content of the web pages.
  - **CSS**: Styling of the web pages.
  - **Bootstrap**: Mobile-first, responsive UI design.

- **Backend**:
  - **Django**: Python framework for handling server-side logic, user requests, and database management.

- **Database**:
  - **SQLite**: Lightweight, serverless database used for storing recipe data.

---

## **Key Features**
1. **Create Recipes**:
   - Add new recipes with ingredients, preparation steps, and images.
  
2. **View Recipes**:
   - Display all recipes in a list, showcasing details for each recipe.

3. **Update Recipes**:
   - Edit existing recipes, allowing users to update ingredients, instructions, or images.

4. **Delete Recipes**:
   - Dynamically delete recipes directly from the frontend interface.

5. **Search Recipes**:
   - Implemented a search function that filters recipes based on a keyword.

6. **Image Rendering**:
   - Users can upload and view images associated with each recipe.

---

## **Development Highlights**
1. **Handling Static Media Files**:
   - Managed static files (images) and configured the necessary settings for proper handling in Django.
   - Ensured images were rendered correctly in the frontend.

2. **Data Management**:
   - Used the **POST method** for sending data to the database.
   - Overcame challenges with passing URL parameters during deletion, resolving them by passing the URL as an integer.

3. **Search Functionality**:
   - Implemented a search feature using Django's query lookups.
   - Utilized **`icontains`** for case-insensitive searches based on substrings.

4. **Data Update Mechanism**:
   - Learnt how to update recipe data dynamically while ensuring proper page redirection after updates.

---

## **Git & GitHub**

1. **Git Version Control**:
   - The project is maintained using **Git** for version control.

2. **GitHub Repository**:
   - [RecipeVault GitHub Repository](https://github.com/sandip3/RecipeVault-)

3. **Clone the Repository**:
   - Clone the repository using the following command:
   ```bash
   git clone https://github.com/sandip3/RecipeVault-.git
   ```

4. **Commit Changes**:
   - To commit changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```

---

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sandip3/RecipeVault-.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Core
   ```

3. **Install dependencies**:
   - Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   - Set up the database:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional):
   - Create an admin user to access Django’s admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the app**:
   - Open your browser and go to:
   ```url
   http://127.0.0.1:8000/
   ```

---

## **Contributing**

1. **Fork the repository**:
   - Fork the repository to make your changes, and submit a pull request.

2. **Submit issues**:
   - Report bugs, issues, or feature requests via GitHub issues section.

3. **Enhance the app**:
   - Contribute by adding new features or fixing bugs.

4. **Code of Conduct**:
   - Please maintain a respectful code of conduct when contributing to this project.

---
## **Screenshots**

1. **Recipe View and Search Page**  

   ![Recipe View and Search Page Screenshot](./IMG/Receipe%20App.png)

---

## **Connect with me:**

- [LinkedIn](https://www.linkedin.com/in/sandip-mishra333/)
- [GitHub](https://github.com/sandip3/)

---

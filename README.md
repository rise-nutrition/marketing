# Rise Nutrition Marketing Site

## Design

The Design is built off of [Material Kit PRO](https://www.creative-tim.com/product/material-kit-pro). If you need 
access to these assets, please let someone know.

The goal is to stick to a Material-based design, because it looks smoother and cleaner compared to other 
designs.

## Getting Started

The app uses Python Flask to run, and NodeJS to compile the SCSS to CSS. We assume you already 
have them installed, or can install them yourself.

### Setting up Virtual Environment & Node Modules

Run the following to get the Python portion of the project set up.

```bash
# Create the virtual environment
$ virtualenv venv
# Tell your shell to use the virtualenv instead of system Python
$ source venv/bin/activate
# Install dependencies
$ pip install -r requirements.txt
```

Run the following to get the `npm` portion of the project set up.

```bash
$ npm install
```

### Compiling the Sass Files

This only needs to be done after you make changes to the styles.

```bash
$ npm run scss
```

### Running the App

```bash
$ FLASK_APP=main FLASK_ENV=development flask run
```
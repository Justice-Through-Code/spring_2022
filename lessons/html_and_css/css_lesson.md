# Outline

We are going to learn:

-   How to add styles to an HTML document using `style` tags
-   How to add styles to HTML elements using the `style` attribute
-   CSS selectors
-   CSS classes and ids
-   Organizing styles in a CSS file

# Introduction

CSS stands for Cascading Style Sheets, a language that helps us define the appearance of web pages by targeting HTML elements and applying styles to them.

# Add styles to your HTML file

-   Create a new HTML file called `styles_practice.html`
-   Add the following HTML

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>My styled page</title>
    </head>
    <body>
        <h1>Hello world</h1>
        <p>I'm learning HTML and CSS</p>
    </body>
</html>
```

Inside `<head>` add the following:

```html
<style>
    h1 {
        color: blue;
    }
</style>
```

-   Explain that `h1` is a CSS selector and it affects all the `<h1>` in this HTML document
-   Explain that `color` is a CSS property, `blue` is the value.
    -   There can be multiple property-value pairs to a selector.
    -   The order of properties do not matter

## More CSS properties

```html
<style>
    h1 {
        color: blue;
        text-align: center;
    }
</style>
```

## More CSS selectors

Let's apply styles to other HTML elements

```html
<style>
    h1 {
        color: blue;
        text-align: center;
    }

    p {
        color: blue;
        font-family: verdana;
        font-size: 18px;
    }
</style>
```

# Classes

-   Explain how classes allows us to share styles between HTML elements
-   Explain that class names are made up
    -   Class names begin with a `.`
    -   Class names cannot have spaces
-   Explain that class names are added to an element's `class` attribute.
    -   Class names are separated by spaces here

```html
<style>
    h1 {
        color: blue;
        text-align: center;
    }

    p {
        color: blue;
        font-family: verdana;
        font-size: 18px;
    }

    .blue {
        color: blue;
    }

    .center {
        text-align: center;
    }
</style>

<body>
    <h1 class="blue center"></h1>
    <p class="blue"></p>
</body>
```

Now that we have classes to apply `color: blue` and `text-align: center`, we can remove previous instances of those property-value pairs.

```html
<style>
    p {
        font-family: verdana;
        font-size: 18px;
    }

    .blue {
        color: blue;
    }

    .center {
        text-align: center;
    }
</style>

<body>
    <h1 class="blue center"></h1>
    <p class="blue"></p>
</body>
```

# Ids

-   Explain how ids allow us to target styles to a single HTML element
-   Explain that ids names are made up and follow the same rule as classes except
    -   Id names begin with a `#`
-   Explain that id names are added to an element's `id` attribute.
    -   There can only be one `id` name for an element

```html
<style>
    p {
        font-family: verdana;
        font-size: 18px;
    }

    #title {
        font-size: 48px;
    }

    .blue {
        color: blue;
    }

    .center {
        text-align: center;
    }
</style>

<body>
    <h1 id="title" class="blue center"></h1>
    <p class="blue"></p>
</body>
```

# Style attribute

We can also apply styles to an individual HTML element by using the `style` attribute

-   Explain that the property-value pairs are the same
-   Explain that multiple property-key value pairs are separated by `;` and written in one line
-   Explain that the style attribute should be used sparingly or else it gets unmanageable
-   Explain that style attributes override selectors, classes and Ids

```html
<h1 style="color: red; text-align: right">Hello world</h1>
```

# Creating a CSS file

Explain how adding styles into the `<style>` becomes unmanageable over time and the styles can be moved to a CSS file. There can be multiple CSS files.

-   Create a CSS file, move the styles there
-   Add it to the `<head>` of the HTML file

```html
<link rel="stylesheet" href="styles.css" />
```

-   Revisit relative and absolute path from HTML lesson

## CSS Source Code

Back in Chrome:

-   Right-click an element in the browser and click `Inspect`
-   This opens Chrome's `Developer Tools` and automatically navigates to `Elements`
-   The inspected element should appear highlighted. Depending on your browser, the styles for that element should appear left, right or bottom of the `Elements` view. You can click other elements to show what its styles look like as well
-   Show how CSS selectors, classes, ids appear with CSS property values under them
-   You can do this on any website to see what the CSS for a given element looks like

# Conclusion

You don't have to memorize CSS selectors and properties, it's completely okay to refer to external resources to find what suits your styling needs

-   Google 'CSS properties'
-   Click on [W3Schools CSS reference](https://www.w3schools.com/cssref/)
-   Scroll through the page highlighting the long list of CSS properties
-   Similary, you can google 'CSS selectors' and use [W3School's selectors reference](https://www.w3schools.com/cssref/css_selectors.asp)
-   The goal here is not become a 'HTML/CSS expert', but to feel comfortable enough to work with these to develop a full-stack app with Django

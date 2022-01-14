# Outline

We are going to learn:

-   HTML and use it to create a web page
-   Use HTML tags to organize text, links, images and more

# Introduction

HTML stands for Hyper Text Markup Language, a language that helps us define the structure and content of web pages. It is considered a markup language as opposed to a programming language.
* Bring back front-end / back-end discussion here to discuss how HTML is more for the front-end of a website, what users see
# Create an HTML file

-   Open your editor, create a new file and save it as `index.html`
-   Explain that the file extension `.html` is required

## Add content

-   Type some text and save the file

```html
Hello world
```

-   We used the terminal to run our Python code but in the case of HTML all you need is a browser.
-   Let's open `index.html` in Chrome or your preferred browser.
-   You'll notice that it looks like a regular text document.

## Add enclosing tags

Let's make some changes by adding some HTML

```html
<h1>Hello world</h1>
```

Back to your browser, refresh the tab displaying `index.html`

### What's happening?

-   We added an opening and close `<h1>` tag. This turns our content into a heading.
-   By wrapping HTML tags around our content we specify what we want our content to be
-   The combination of tags and content are called HTML elements

# More tags

There are other tags available to us in HTML, let's try some out!

## Text

-   Show tags from heading tags `<h1>` to `<h6>`

```html
<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>
```

-   Show paragraph tags `<p>`

```html
<p>This is a paragraph</p>
```

-   Show ordered list tags `<ol>`, `<li>`

```html
<ol>
    <li>apples</li>
    <li>bananas</li>
    <li>oranges</li>
</ol>
```

-   Show unordered list tags `<ul>`, `<li>`

```html
<ul>
    <li>apples</li>
    <li>bananas</li>
    <li>oranges</li>
</ul>
```

## Comments

-   Show HTML comments

```html
<!-- This is a comment -->
```

## Images

-   Show img tag `<img>`
-   Show `src`, `width`, `height`, `alt` attributes
-   Explain that `<img>` does not have a closing tag

```html
<img
    src="https://i.imgur.com/DSEK2uI.jpeg"
    width="400"
    height="400"
    alt="debugging meme"
/>
```

You can also add images from your computer! In the directory where you created `index.html`, put any programming meme image you like from the internet. When you're done, add the file path of the image in the `src` attribute:

```html
<img src="meme.jpg" width="400" height="400" alt="debugging meme" />
```

This tells our `img` tag that the file is located in the same folder as the current page

### More on file paths

It might seem as simple as adding the file name `meme.jpg` to get the image to load but we're actually applying the rules of file paths. Let's look at how the file path would change depending if `meme.jpg` was located somewhere else:

| Path                           | Description                                                                                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<img src="images/meme.jpg">`  | The "meme.jpg" file is located in the images folder in the current folder                                                                                                   |
| `<img src="../meme.jpg">`      | The "meme.jpg" file is located in the folder one level up from the current folder                                                                                           |
| `<img src="/images/meme.jpg">` | The "meme.jpg" file is located in the images folder at the root of the current web server. Don't worry about this yet. It's relevant once we get into building web servers! |

## Hyperlinks

-   Show hyperlink tag `<a>`
-   Show `href` attribute. An HTML `attribute` is a special keyword that allows us to modify the specific behavior of an HTML element
-   Explain that `<a>` tags can wrap other tags to turn it into a hyperlink
-   You can link to other HTML pages on your computer! The rules of file paths apply here too!

```html
<a href="https://www.google.com/">Go to google</a>
```

```html
<a href="https://www.github.com/">
    <h4>Go to Github instead</h4>
</a>
```

## Forms

-   Show form tag `<form>`,
-   Show how the form tag can wrap other tags. The ones we will explore are:
    -   Input tag `<input>` with different values set to `type`
    -   Label tag `<label>`
    -   Button tag `<button>`
-   Explain that submitting this form isn't sending the data anywhere. We will visit this in future lessons.

```html
<form>
    <label for="fullname">Full Name:</label>
    <input name="fullname" type="text" value="" placeholder="E.g. John Doe" />
    <label for="age">Age:</label>
    <input name="age" type="number" value="" placeholder="E.g. 18" />
    <button type="submit">Submit</button>
</form>
```

# HTML document anatomy

-   Show how the typical HTML page is structured

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>My test page</title>
    </head>
    <body>
        <!-- content goes here -->
    </body>
</html>
```

-   The `<head>` contains all the metadata. Metadata is data (information) about data. So in this case, it describes the contents of the HTML document
    -   Show `<title>`
-   The `<body>` contains all the content

## HTML Source Code

Back in Chrome:

-   Right-click an element in the browser and click `Inspect`
-   This opens Chrome's `Developer Tools` and automatically navigates to `Elements`
-   The inspected element should appear highlighted. Scroll to show rest of the HTML source code.
-   You can do this on any website to see what the HTML looks like

# Conclusion

You don't have to memorize HTML tags, it's completely okay to refer to external resources to find exactly what you need for your content

-   Google 'HTML tags'
-   Click on [W3Schools HTML reference](https://www.w3schools.com/tags/default.asp)
-   Scroll through the page highlighting the long list of HTML tags

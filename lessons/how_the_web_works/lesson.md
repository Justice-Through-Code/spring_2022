# How the web works

## Outline

We are going to learn about:

-   The key components of the web and how they come together to create the experience of surfing the web

# Visiting a website

![Screen Recording 2021-10-09 at 08 55 37 AM](https://user-images.githubusercontent.com/7483633/136658703-5297a903-5888-4a50-a6a9-3beb5761f7ff.gif)

Let's start somewhere familiar: typing a URL like `github.com` in the address bar of your browser and pressing enter. Eventually the Github homepage loads.

From the time we press enter to seeing the page load, there is plenty happening under the hood: We take a whole roundtrip around the web and make many stops on the way. Let's take a closer look!

# Client and Server

![client and server](https://madooei.github.io/cs421_sp20_homepage/assets/client-server-1.png)

The act of visiting a website boils down to two computers talking to each other: **the client and the server.**

-   The client is like an application like your browser connected to the internet
-   The server is the computer that stores the website
-   The "talking" involves a client requesting for a resource and the server responding with the resource. So, when you type a URL like `github.com`, the browser is requesting the homepage from the Github server and the server eventually responds with the homepage.

# Let's take a trip over the web...

But there's more to it. Let's see what happens we type the URL and press enter:

## The browser looks up Github’s IP address

![dns converts domain to ip](https://sitechecker.pro/wp-content/uploads/2019/09/domain-to-ip.jpg)

An **IP address** is a unique identifier of a computer connected to the internet. If you're watching this video, your device is connected to the internet, therefore you have one too!

In order to look up Github's IP address, the browser does a DNS look-up. The DNS (Domain Name System) is a service that translates a domain like `github.com` into an IP address. It is like the address book for the web!

## The browser uses the IP address to establish a TCP connection with the Github server

A TCP connection converts messages into small chunks called packets and ensures that messages are received in order and not lost.

## The browser requests the Github homepage from the Github server

The browser uses HTTP - the language shared by the client and server - to request for the Github homepage resource.

Client Request:

```
GET / HTTP/2
Host: github.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```

Server Response:

```
HTTP/2 200 OK
server: GitHub.com
date: Sat, 09 Oct 2021 13:11:00 GMT
content-type: text/html; charset=utf-8
vary: X-PJAX, X-PJAX-Container, Accept-Language, Accept-Encoding, Accept, X-Requested-With
permissions-policy: interest-cohort=()
content-language: en-US
etag: W/"561cfaa4966e19a9ecbfaf36381a6b8a"
cache-control: max-age=0, private, must-revalidate
strict-transport-security: max-age=31536000; includeSubdomains; preload
...
```

## The Github server responds with the homepage resource

..in the form of an HTML document. An HTML document defines the structure and content of a web page.

## The browser constructs the homepage

The browser loads the HTML document. The browser then asks for additional resources like:

-   CSS which defines the appearance of the page
-   and Javascript which defines the behavior of the homepage like button clicks and pop ups.

The browser takes these resources and constructs rest of the Github homepage!

# Conclusion

-   So to recap, we saw a birds eye view of what happens when we visit a website and the many trips we make along the way. Although it's not important that you're super thorough with these concepts, it'll help us understand website development and deployment a lot better

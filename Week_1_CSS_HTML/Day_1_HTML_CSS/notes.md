# Advanced CSS


## Elements Position
position:  
* `static`: Default value. Elements render in order, as they appear in the document flow  
* `relative`: The element is positioned relative to its normal position; you can add left, right, top or bottom arguments to add a gap by the element.  
* `fixed`: Always stays in the same place even if the page is scrolled, left, right, top and bottom are used to position the element  
* `absolute`: The element is positioned relative to its first positioned (not static) ancestor element  
* `sticky`: The element is positioned based on the user’s scroll position


## Overflow
The `overflow` property specifies whether to clip the content or add scrollbars when an element’s content is too big to fit in the specified area.  

* `visible`:  Default. The overflow is not clipped. The content renders outside the element’s box
* `hidden`: The overflow is clipped, and the rest of the content will be invisible
* `scroll`: The overflow is clipped, and a scrollbar is added to see the rest of the content
* `auto`: Similar to scroll, but it adds scrollbars only when necessary

## Pseudo Class Selectors
A pseudo-class is used to style an element when he is in a special state.  
The syntax is : `element:pseudo-class {...}`

`hover` means “mouse is over it”
```css
div:hover {
  background-color: blue;
}
```

To style `<p>` tags that are the first child of another element, use:
```css
p:first-child{
  color: blue;
}
```

The `not` pseudo-class allows you to exclude elements; for example, select all the divs that are not of the `ignore` class.
```css
div:not(.ignore){
    background-color: yellow;
}
```

## Media Queries
### Cheat Sheet
```css
/*------------------------------------------
  Responsive Grid Media Queries - 1280, 1024, 768, 480
   1280-1024   - desktop (default grid)
   1024-768    - tablet landscape
   768-480     - tablet 
   480-less    - phone landscape & smaller
--------------------------------------------*/
@media all and (min-width: 1024px) and (max-width: 1280px) { }

@media all and (min-width: 768px) and (max-width: 1024px) { }

@media all and (min-width: 480px) and (max-width: 768px) { }

@media all and (max-width: 480px) { }
```

### Example
```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <h1>Media Queries</h1>
    <div id="div1"></div>
    <div id="div2"></div>
    <div id="div3"></div>
    <div id="div4"></div>
</body>
</html>
```

```css
div {
    height: 100px;
}

#div1 {
    background-color: red;
}

#div2 {
    background-color: blue;
}

#div3 {
    background-color: green;
}

#div4 {
    background-color: purple;
}

//The logical keywords "not" or "only" can be used optionally to include or exclude specific media types or screen sizes
@media only screen and (min-width: 600px) {
    div {
        width: 100%;
    }
}


@media only screen and (min-width: 900px) {
    div {
        width: 50%;
        float: left;
    }
}

@media only screen and (min-width: 1200px) {
    div {
        width: 25%;
        float: left;
    }
}
```


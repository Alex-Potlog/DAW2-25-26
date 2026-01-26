// --DomElement--
// Main Class
class DomElement {
    #attr //object
    #tag //string
    #element //html element
    constructor(attr, tag) {
        this.#tag = tag
        this.#attr = attr
        this.#element = undefined
        return this
    }
    get attr() {
        return this.#attr
    }
    createElement() {
        this.#element = document.createElement(this.#tag)
        for (const attribute in this.#attr) {
            this.#element.setAttribute(attribute, this.#attr[attribute])
        }
        console.dir(this.#element)
        return this
    }
    printElement(pos = { id: 'content', position: 'beforeend' }) {
        document.querySelector(`#${pos.id}`).insertAdjacentElement(pos.position, this.#element)
        return this
    }
    deleteElement() {
        this.#element.remove()
        return this
    }
    addListener(event, func) {
        this.#element.addEventListener(event, func)
        return this
    }


}
// --InlineElement--
// class to build html element with text inside
class inlineElement extends DomElement {
    constructor(attr, tag, text) {
        super(attr, tag)
        this.text = text
    }
    createElement() {
        super.createElement()
        this.element.innerText = this.text
        // con createTextNode:
        // const textNode = document.createTextNode(this.text)
        // this.element.appendChild(textNode)
        return this
    }
}


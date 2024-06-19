#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h)) {
      this.width = undefined;
      this.height = undefined;
    } else if (w < 1 || h < 1) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;

/*
 * Copyright 2013 The Polymer Authors. All rights reserved.
 * Use of this source code is governed by a BSD-style
 * license that can be found in the LICENSE file.
 */

var assert = chai.assert;

var thisFile = 'test.main.js';
var base;
(function() {
  var s$ = document.querySelectorAll('script[src]');
  Array.prototype.forEach.call(s$, function(s) {
    var src = s.getAttribute('src');
    var re = new RegExp(thisFile + '[^\\\\]*');
    var match = src.match(re);
    if (match) {
      base = src.slice(0, -match[0].length);
    }
  });
})();

function expectStructure(nodeOrWrapper, nonNullFields) {
  assert(nodeOrWrapper);
  assert.strictEqual(nodeOrWrapper.parentNode, nonNullFields.parentNode || null);
  assert.strictEqual(nodeOrWrapper.previousSibling,
      nonNullFields.previousSibling || null);
  assert.strictEqual(nodeOrWrapper.nextSibling, nonNullFields.nextSibling || null);
  assert.strictEqual(nodeOrWrapper.firstChild, nonNullFields.firstChild || null);
  assert.strictEqual(nodeOrWrapper.lastChild, nonNullFields.lastChild || null);
}

function unwrapAndExpectStructure(node, nonNullFields) {
  for (var p in nonNullFields) {
    nonNullFields[p] = ShadowDOMPolyfill.unwrap(nonNullFields[p]);
  }
  expectStructure(ShadowDOMPolyfill.unwrap(node), nonNullFields);
}

function assertArrayEqual(a, b, msg) {
  for (var i = 0; i < a.length; i++) {
    assert.equal(a[i], b[i], msg);
  }
  assert.equal(a.length, b.length, msg);
}

mocha.setup({
  ui: 'tdd',
  globals: ['console', 'getInterface']
})

var modules = [
  'Comment.js',
  'Document.js',
  'Element.js',
  'HTMLBodyElement.js',
  'HTMLContentElement.js',
  'HTMLHeadElement.js',
  'HTMLShadowElement.js',
  'HTMLTemplateElement.js',
  'MutationObserver.js',
  'Node.js',
  'ParentNodeInterface.js',
  'ShadowRoot.js',
  'Text.js',
  'Window.js',
  'custom-element.js',
  'events.js',
  'paralleltrees.js',
  'reprojection.js',
  'rerender.js',
  'test.js',
  'wrappers.js',
];

modules.forEach(function(inSrc) {
  document.write('<script src="' + base + 'js/' + inSrc + '"></script>');
});

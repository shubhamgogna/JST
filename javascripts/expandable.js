/**
 * Adapted from example at
 * http://jsfiddle.net/hungerpain/eK8X5/7/
 **/
function makeCollapseable(object) {
  container = $(object);
  container.children(":first").click(createToggleCallback(container));
}

function createToggleCallback(parent) {
  return function() {
    parent.children(".content").slideToggle(600);
  }
}

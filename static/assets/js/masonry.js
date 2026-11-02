$(document).ready(function() {
  // Init Masonry
  var $grid = $('.grid').masonry({
    gutter: 10,
    horizontalOrder: true,
    itemSelector: '.grid-item',
  });
  // Layout Masonry after each image loads
  $grid.imagesLoaded().progress( function() {
    $grid.masonry('layout');
  });
  // Layout Masonry again once the web font loads, since titles can change height
  document.fonts.ready.then(function() {
    $grid.masonry('layout');
  });
});

function ImageAutoResize() {
  // start image process only when loading is completed
  if (document.readyState != "complete") {
    setTimeout(arguments.callee, 100);
    return;
  }

  // find out the container width, height, proportaion
  var containter_width = null;
  if ($('#blog_main_area').width()) {
    containter_width = $('#blog_main_area').width();
  }
  else {
    containter_width = $('article.content').width();
  }

  var containter_height = null;
  if ($('#blog_main_area').height()) {
    containter_height = $('#blog_main_area').width();
  }
  else {
    containter_height = $('article.content').width();
  }
  if (containter_height > $(window).height()) {
    containter_height = $(window).height();
  }

  ContainerProportion = containter_width / containter_height;

  $("section#blog img").each(function () {
    // resize imgs to fit window and container, and also put them center
    var PhotoProportion = $(this).width() / $(this).height();
    var TargetWidth;
    if (PhotoProportion < ContainerProportion) {
      TargetWidth = containter_height*PhotoProportion*0.8;
    }
    else {
      TargetWidth = containter_width;
    }
    if (this.width > TargetWidth) {
      if ($(this).parents('a').length === 0) {
        $(this).wrap(
          $('<a/>').attr('href', $(this).attr('src'))
        );
      }

      $(this).css('width', TargetWidth)
        .css('height', '')
        .css('display', 'block')
        .css('margin', '0 auto');
    }
  });
}

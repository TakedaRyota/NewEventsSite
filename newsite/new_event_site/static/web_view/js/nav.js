/* =========================
ナビゲーションバーの動作
============================ */

$(function() {
  /**
   * ハンバーガーメニュー押下時
   */
  $('.hamburger-menu').on('click', function() {
    $(this).toggleClass('active');
    $('.navbar-nav, .top-logo').toggleClass('active');
    return false;
  });

  /**
   * スクロール時にTOPへボタンを表示する
   */
  const $scrollTopBtn = $('.scroll-top');
  $(window).scroll(function () {
    if ($(this).scrollTop() > $(window).height() / 2) {  //100pxスクロールしたら表示
      $scrollTopBtn.fadeIn();
    } else {
      $scrollTopBtn.fadeOut();
    }
  });

});
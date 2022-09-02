/* =========================
ナビゲーションバーの動作
============================ */

$(function() {
  /**
   * ハンバーガーメニュー押下時
   */
  $('.hamburger-menu').on('click', function() {
    $(this).toggleClass('active');
    $('.navbar-nav').toggleClass('active');
    return false;
  });
  
});
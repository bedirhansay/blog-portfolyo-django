import $ from "jquery";

$(document).ready(function () {
  $(".linkedin").click(function () {
    shareToLinkedIn();
  });

  $(".twitter").click(function () {
    shareToTwitter();
  });

  $(".instagram").click(function () {
    shareToInstagram();
  });

  function shareToLinkedIn() {
    const urlToShare = "https://your-url-to-share.com";
    window.open(`https://www.linkedin.com/shareArticle?url=${urlToShare}`);
  }

  function shareToTwitter() {
    const urlToShare = "https://your-url-to-share.com";
    window.open(`https://twitter.com/intent/tweet?url=${urlToShare}`);
  }

  function shareToInstagram() {
    const caption = "Check out this post!";
    window.location.href = `https://www.instagram.com/create/caption/?caption=${encodeURIComponent(
      caption
    )}`;
  }
});

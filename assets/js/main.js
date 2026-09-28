/* Essential Shield — site interactions
   Vanilla JS, no dependencies, progressive enhancement only. */
(function () {
  'use strict';

  var FORM_ENDPOINT =
    'https://vision.leadrai.com/api/forms/4dfea5213f838b89b8fd940221481367';

  /* ---------------------------------------------------------------- nav */
  function initNav() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.getElementById('primary-nav');
    if (!toggle || !nav) return;

    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ------------------------------------------------------------- reveal */
  function initReveal() {
    var items = document.querySelectorAll('.reveal');
    if (!items.length) return;
    if (!('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-in');
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: '0px 0px -8% 0px', threshold: 0.08 }
    );
    items.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 70 + 'ms';
      io.observe(el);
    });
  }

  /* ------------------------------------------------------ before/after */
  function initBeforeAfter() {
    document.querySelectorAll('[data-ba]').forEach(function (root) {
      var range = root.querySelector('.ba__range');
      var after = root.querySelector('.ba__after');
      var handle = root.querySelector('.ba__handle');
      var arrows = root.querySelector('.ba__arrows');
      if (!range || !after || !handle) return;

      function paint() {
        var v = Number(range.value);
        after.style.clipPath = 'inset(0 0 0 ' + v + '%)';
        handle.style.left = v + '%';
        if (arrows) arrows.style.left = v + '%';
      }
      range.addEventListener('input', paint);
      paint();
    });
  }

  /* --------------------------------------------------------- year stamp */
  function initYear() {
    var y = String(new Date().getFullYear());
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = y;
    });
  }

  /* --------------------------------------------------------------- forms */
  function showStatus(form, type, message) {
    var box = form.querySelector('.form-status');
    if (!box) {
      window.alert(message);
      return;
    }
    box.className =
      'form-status is-visible form-status--' + (type === 'ok' ? 'ok' : 'err');
    box.textContent = message;
    box.setAttribute('role', 'status');
    try {
      box.scrollIntoView({ behavior: 'smooth', block: 'center' });
    } catch (e) {
      box.scrollIntoView();
    }
  }

  function initForms() {
    var forms = document.querySelectorAll('form[data-leadr]');

    // Stamp the current page URL into every hidden _page field.
    document.querySelectorAll('input[name="_page"]').forEach(function (input) {
      input.value = window.location.href;
    });

    forms.forEach(function (form) {
      form.addEventListener('submit', function (e) {
        // Let the browser handle native validation first.
        if (typeof form.checkValidity === 'function' && !form.checkValidity()) {
          return;
        }
        e.preventDefault();

        var button = form.querySelector('button[type="submit"]');
        var originalLabel = button ? button.textContent : '';
        if (button) {
          button.disabled = true;
          button.textContent = 'Sending…';
        }

        var payload = {};
        new FormData(form).forEach(function (value, key) {
          if (payload[key] !== undefined) {
            payload[key] = [].concat(payload[key], value);
          } else {
            payload[key] = value;
          }
        });
        payload._page = window.location.href;

        fetch(FORM_ENDPOINT, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json'
          },
          body: JSON.stringify(payload)
        })
          .then(function (res) {
            return res.json().catch(function () {
              return { ok: res.ok };
            });
          })
          .then(function (data) {
            if (data && data.ok) {
              form.reset();
              document
                .querySelectorAll('input[name="_page"]')
                .forEach(function (input) {
                  input.value = window.location.href;
                });
              showStatus(
                form,
                'ok',
                'Thanks, your message was sent. The Essential Shield team will be in touch shortly — for anything urgent call 0411 750 250.'
              );
            } else {
              throw new Error('Submission rejected');
            }
          })
          .catch(function () {
            showStatus(
              form,
              'err',
              'Sorry — we could not send that just now. Please call 0411 750 250 or email naturally@essentialshield.com.'
            );
          })
          .then(function () {
            if (button) {
              button.disabled = false;
              button.textContent = originalLabel;
            }
          });
      });
    });

    // Plain (no-JS-path) submissions come back with ?submitted=1
    var params = new URLSearchParams(window.location.search);
    if (params.get('submitted') === '1') {
      var target =
        document.querySelector('form[data-leadr] .form-status') || null;
      if (target) {
        var formEl = target.closest('form');
        showStatus(
          formEl,
          'ok',
          'Thanks, your message was sent. The Essential Shield team will be in touch shortly — for anything urgent call 0411 750 250.'
        );
      }
    }
  }

  function ready(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  ready(function () {
    initNav();
    initReveal();
    initBeforeAfter();
    initYear();
    initForms();
  });
})();

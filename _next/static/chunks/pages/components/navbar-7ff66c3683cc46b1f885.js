(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[437],{2167:function(e,n,t){"use strict";var r=t(3038),o=t(862);n.default=void 0;var a=o(t(7294)),c=t(9414),i=t(4651),u=t(7426),l={};function s(e,n,t,r){if(e&&(0,c.isLocalURL)(n)){e.prefetch(n,t,r).catch((function(e){0}));var o=r&&"undefined"!==typeof r.locale?r.locale:e&&e.locale;l[n+"%"+t+(o?"%"+o:"")]=!0}}var f=function(e){var n,t=!1!==e.prefetch,o=(0,i.useRouter)(),f=a.default.useMemo((function(){var n=(0,c.resolveHref)(o,e.href,!0),t=r(n,2),a=t[0],i=t[1];return{href:a,as:e.as?(0,c.resolveHref)(o,e.as):i||a}}),[o,e.href,e.as]),d=f.href,_=f.as,p=e.children,v=e.replace,h=e.shallow,m=e.scroll,g=e.locale;"string"===typeof p&&(p=a.default.createElement("a",null,p));var b=(n=a.Children.only(p))&&"object"===typeof n&&n.ref,H=(0,u.useIntersection)({rootMargin:"200px"}),y=r(H,2),E=y[0],L=y[1],C=a.default.useCallback((function(e){E(e),b&&("function"===typeof b?b(e):"object"===typeof b&&(b.current=e))}),[b,E]);(0,a.useEffect)((function(){var e=L&&t&&(0,c.isLocalURL)(d),n="undefined"!==typeof g?g:o&&o.locale,r=l[d+"%"+_+(n?"%"+n:"")];e&&!r&&s(o,d,_,{locale:n})}),[_,d,L,g,t,o]);var w={ref:C,onClick:function(e){n.props&&"function"===typeof n.props.onClick&&n.props.onClick(e),e.defaultPrevented||function(e,n,t,r,o,a,i,u){("A"!==e.currentTarget.nodeName||!function(e){var n=e.currentTarget.target;return n&&"_self"!==n||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.nativeEvent&&2===e.nativeEvent.which}(e)&&(0,c.isLocalURL)(t))&&(e.preventDefault(),null==i&&r.indexOf("#")>=0&&(i=!1),n[o?"replace":"push"](t,r,{shallow:a,locale:u,scroll:i}))}(e,o,d,_,v,h,m,g)},onMouseEnter:function(e){(0,c.isLocalURL)(d)&&(n.props&&"function"===typeof n.props.onMouseEnter&&n.props.onMouseEnter(e),s(o,d,_,{priority:!0}))}};if(e.passHref||"a"===n.type&&!("href"in n.props)){var x="undefined"!==typeof g?g:o&&o.locale,k=o&&o.isLocaleDomain&&(0,c.getDomainLocale)(_,x,o&&o.locales,o&&o.domainLocales);w.href=k||(0,c.addBasePath)((0,c.addLocale)(_,x,o&&o.defaultLocale))}return a.default.cloneElement(n,w)};n.default=f},7426:function(e,n,t){"use strict";var r=t(3038);n.__esModule=!0,n.useIntersection=function(e){var n=e.rootMargin,t=e.disabled||!c,u=(0,o.useRef)(),l=(0,o.useState)(!1),s=r(l,2),f=s[0],d=s[1],_=(0,o.useCallback)((function(e){u.current&&(u.current(),u.current=void 0),t||f||e&&e.tagName&&(u.current=function(e,n,t){var r=function(e){var n=e.rootMargin||"",t=i.get(n);if(t)return t;var r=new Map,o=new IntersectionObserver((function(e){e.forEach((function(e){var n=r.get(e.target),t=e.isIntersecting||e.intersectionRatio>0;n&&t&&n(t)}))}),e);return i.set(n,t={id:n,observer:o,elements:r}),t}(t),o=r.id,a=r.observer,c=r.elements;return c.set(e,n),a.observe(e),function(){c.delete(e),a.unobserve(e),0===c.size&&(a.disconnect(),i.delete(o))}}(e,(function(e){return e&&d(e)}),{rootMargin:n}))}),[t,n,f]);return(0,o.useEffect)((function(){if(!c&&!f){var e=(0,a.requestIdleCallback)((function(){return d(!0)}));return function(){return(0,a.cancelIdleCallback)(e)}}}),[f]),[_,f]};var o=t(7294),a=t(3447),c="undefined"!==typeof IntersectionObserver;var i=new Map},4705:function(e,n,t){"use strict";t.r(n),t.d(n,{default:function(){return i}});var r=t(5893),o=t(5323),a=t.n(o),c=t(1664);function i(){return(0,r.jsxs)("nav",{className:a().nav,children:[(0,r.jsx)(c.default,{href:"/tutorial",children:(0,r.jsx)("a",{children:"Tutorials"})}),(0,r.jsx)(c.default,{href:"/docs",children:(0,r.jsx)("a",{children:"Docs"})})]})}},351:function(e,n,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/components/navbar",function(){return t(4705)}])},5323:function(e){e.exports={container:"Home_container__1EcsU",main:"Home_main__1x8gC",nav:"Home_nav__1c1C3",landing:"Home_landing__3VX3f",section:"Home_section__16Giz",text:"Home_text__1sCQa",button:"Home_button__Xc9mA",col_card:"Home_col_card__3Qeme",col4:"Home_col4__soLh1",footer:"Home_footer__1WdhD",description:"Home_description__17Z4F",grid:"Home_grid__2Ei2F",card:"Home_card__2SdtB",logo:"Home_logo__1YbrH"}},1664:function(e,n,t){e.exports=t(2167)}},function(e){e.O(0,[774,888,179],(function(){return n=351,e(e.s=n);var n}));var n=e.O();_N_E=n}]);
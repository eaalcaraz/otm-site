/* On Time Maintenance — site behaviour. Edit the two lines below before launch. */
var OTM = {
  FORM_ENDPOINT: "https://formspree.io/f/maeylpkj", /* 1. paste your Formspree form endpoint */
  EMAIL: "ontimephx@gmail.com"                            /* 2. the address you actually control */
};

(function(){
  /* ----- email is set in exactly one place ----- */
  document.querySelectorAll('[data-email]').forEach(function(el){
    if(el.tagName==='A') el.href = 'mailto:'+OTM.EMAIL;
    var target = el.querySelector('b') || el;
    if(!target.children.length) target.textContent = OTM.EMAIL;
  });

  /* ----- header + menu ----- */
  var burger=document.getElementById('burger'),close=document.getElementById('closeBtn'),
      menu=document.getElementById('menu'),scrim=document.getElementById('scrim'),
      hdr=document.getElementById('hdr'),sticky=document.getElementById('sticky');
  if(burger&&menu){
    function open(){
      menu.hidden=false;scrim.hidden=false;
      requestAnimationFrame(function(){menu.classList.add('open');scrim.classList.add('open')});
      burger.setAttribute('aria-expanded','true');close.setAttribute('aria-expanded','true');document.body.classList.add('locked');
      menu.querySelector('a').focus();
    }
    function shut(){
      menu.classList.remove('open');scrim.classList.remove('open');
      burger.setAttribute('aria-expanded','false');close.setAttribute('aria-expanded','false');document.body.classList.remove('locked');
      setTimeout(function(){menu.hidden=true;scrim.hidden=true},420);burger.focus();
    }
    burger.addEventListener('click',function(){menu.classList.contains('open')?shut():open()});
    close.addEventListener('click',shut);scrim.addEventListener('click',shut);
    document.addEventListener('keydown',function(e){
      if(!menu.classList.contains('open'))return;
      if(e.key==='Escape')shut();
      if(e.key==='Tab'){
        var f=menu.querySelectorAll('a,button'),first=f[0],last=f[f.length-1];
        if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}
        else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}
      }
    });
    /* mark current page */
    var here=location.pathname.replace(/\/$/,'')||'/';
    menu.querySelectorAll('.panel-nav a').forEach(function(a){
      var p=a.getAttribute('href').replace(/\/$/,'')||'/';
      if(p===here||(here==='/index'&&p==='/'))a.setAttribute('aria-current','page');
    });
  }
  window.addEventListener('scroll',function(){
    if(hdr)hdr.classList.toggle('pinned',window.scrollY>80);
    if(sticky){var d=window.scrollY/(document.body.scrollHeight-window.innerHeight);
      sticky.classList.toggle('show',d>.12&&d<.92);}
  },{passive:true});

  /* ----- accordions ----- */
  document.querySelectorAll('.acc button').forEach(function(b){
    b.addEventListener('click',function(){
      var body=b.nextElementSibling,on=b.getAttribute('aria-expanded')==='true';
      b.setAttribute('aria-expanded',!on);
      body.style.maxHeight=on?null:body.scrollHeight+'px';
    });
  });

  /* ----- work request form ----- */
  var form=document.getElementById('wr'); if(!form)return;
  var phone=document.getElementById('phone');
  phone.addEventListener('input',function(){
    var v=phone.value.replace(/\D/g,'').slice(0,10);
    phone.value=v.length>6?'('+v.slice(0,3)+') '+v.slice(3,6)+'-'+v.slice(6):v.length>3?'('+v.slice(0,3)+') '+v.slice(3):v;
  });
  var emg=document.getElementById('emg');
  document.querySelectorAll('input[name="urgency"]').forEach(function(r){
    r.addEventListener('change',function(){emg.classList.toggle('show',r.value==='Emergency'&&r.checked)});
  });
  function bad(el){
    var f=el.closest('.field'),v=(el.value||'').trim(),ok=true;
    if(el.type==='checkbox')ok=el.checked;
    else if(el.type==='email')ok=/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v);
    else if(el.type==='tel')ok=v.replace(/\D/g,'').length===10;
    else if(el.id==='desc')ok=v.length>=15;
    else ok=v.length>0;
    f.classList.toggle('invalid',!ok);return !ok;
  }
  var req=['name','phone','email','addr','desc','consent'].map(function(i){return document.getElementById(i)});
  req.forEach(function(el){el.addEventListener('blur',function(){bad(el)})});

  form.addEventListener('submit',function(e){
    e.preventDefault();
    var first=null;req.forEach(function(el){if(bad(el)&&!first)first=el});
    if(first){first.focus();return}
    var btn=document.getElementById('sub'),fail=document.getElementById('fail');
    btn.textContent='Submitting…';btn.disabled=true;fail.classList.remove('show');
    var d=new Date(),id='OTM-'+String(d.getMonth()+1).padStart(2,'0')+String(d.getDate()).padStart(2,'0')+'-'+String(Math.floor(Math.random()*9000+1000));
    var fd=new FormData(form);fd.append('request_id',id);
    var urg=fd.get('urgency')||'';fd.append('_subject',(urg==='Emergency'?'EMERGENCY — ':'')+'Work request '+id+' — '+(fd.get('name')||''));
    fetch(OTM.FORM_ENDPOINT,{method:'POST',body:fd,headers:{'Accept':'application/json'}})
      .then(function(r){if(!r.ok)throw new Error(r.status);
        document.getElementById('rid').textContent='Request #'+id;
        form.style.display='none';
        var done=document.getElementById('done');done.classList.add('show');done.focus();
        done.scrollIntoView({block:'center',behavior:'smooth'});})
      .catch(function(){btn.textContent='Submit work request';btn.disabled=false;fail.classList.add('show');});
  });
})();

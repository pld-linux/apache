Summary:	HTTP server daemon to provide WWW services with IPv6 support
Summary(de):	Leading World Wide Web-Server
Summary(fr):	Serveur Web leader du marché
Summary(pl):	Serwer WWW (World Wide Web) ze wsparciem dla IPv6
Summary(tr):	Lider WWW tarayýcý
Name:		apache
Version:	1.3.6
Release:	2
Group:		Networking/Daemons
Group(pl):	Sieci/Demony
Source0:	ftp://ftp.apache.org/apache/dist/%{name}_%{version}.tar.gz
Source1:	apache.init
Source2:	%{name}.logrotate
Source3:	%{name}-extra1.tar.bz2
########	http://stonecold.unity.ncsu.edu/software/mod_auth_kerb
#Source5:	mod_auth_kerb-4.3.tar.gz
Source6:	apache_1.3.6.tar.gz.asc
Source7:	apache_1.3.6.tar.gz.md5
Source8:	apache.sysconfig
Patch0:		%{name}-suexec.patch
Patch1:		%{name}_1.3.6.ipv6.patch
Patch2:		%{name}-htdocs.patch
Patch3:		%{name}-release.patch
Copyright:	BSD-like
Obsoletes:	apache-extra
Obsoletes:	apache6
Provides:	httpd
Provides:	webserver
Prereq:		/sbin/chkconfig
URL:		http://www.apache.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Apache is a full featured web server that is freely available, and also
happens to be the most widely used. This version supports IPv6.

%description -l de
Apache ist ein voll funktionsfähiger Web-Server, der kostenlos
erhältlich und weit verbreitet ist.

%description -l fr
Apache est un serveur Web complet, disponible librement, et se trouve être
aussi le plus utilisé à travers le monde.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj±c ten pakiet bêdziesz 
móg³ prezentowaæ w³asne strony WWW w sieci internet. Apache umo¿liwia równie¿
konfigurowanie serwerów wirtualnych. Ta wersja wspiera IPv6.

%description -l tr
Apache serbest daðýtýlan ve çok kullanýlan yetenekli bir web sunucusudur.

%package	suexec
Summary:	Apache suexec wrapper
Summary(pl):	Suexec wrapper do serwera www Apache
Group:		Networking/Development
Group(pl):	Sieci/Programowanie
Requires:	%{name} = %{version}

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and SSI
programs under user IDs different from the user ID of the calling web-server.
Normally, when a CGI or SSI program executes, it runs as the same user 
who is running the web server. 

%description -l pl suexec
SuEXEC umo¿liwia serwerowi Apache uruchamianie programów CGI i SSI z innym
UID ni¿ wywo³uj±cy je serwer. Normalnie programy CGI i SSI s± wykonywane
jako taki sam u¿ytkownik jak serwer WWW.

%package	devel
Summary:	Apache include files
Summary(pl):	Pliki nag³ówkowe do serwera www Apache
Group:		Networking/Development
Group(pl):	Sieci/Programowanie
Requires:	%{name} = %{version}

%description devel
Apache include files.

%description -l pl devel
Pliki nag³ówkowe dla serwera WWW Apache.

%package	doc
Summary:	Apache dokumentation
Summary(pl):	Dokumentacja do Apache
Group:		Documentation
Group(pl):	Dokumentacja
Requires:	%{name} = %{version}
URL:		http://www.apache.org/

%description doc
Documentation for apache in HTML format.

%description -l pl doc
Dokumentacja do Apache w formacie HTML

%prep 
%setup -q -n apache_%{version} -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
OPTIM="$RPM_OPT_FLAGS" LDFLAGS="-s"\
    ./configure \
	--prefix=%{_prefix} \
	--sysconfdir=/etc/httpd \
	--datadir=/home/httpd \
	--libexecdir=/usr/lib/apache \
	--localstatedir=/var \
	--runtimedir=/var/run \
	--logfiledir=/var/log/httpd \
	--without-confadjust \
	--enable-module=all \
	--enable-shared=max \
	--proxycachedir=/var/cache/www/apache \
	--with-perl=%{_bindir}/perl \
	--enable-suexec \
	--suexec-caller=http \
	--suexec-uidmin=500 \
	--suexec-gidmin=500 \
	--sbindir=%{_sbindir} \
	--includedir=%{_includedir}/apache \
	--enable-rule=INET6 
make

%install
rm -rf $RPM_BUILD_ROOT

make install-quiet root="$RPM_BUILD_ROOT"

mv $RPM_BUILD_ROOT/home/httpd/htdocs $RPM_BUILD_ROOT/home/httpd/html

install -d $RPM_BUILD_ROOT/etc/{httpd,logrotate.d,rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT/home/httpd/{html/manual,icons,cgi-bin}
install -d $RPM_BUILD_ROOT/{usr/{lib/apache,sbin,share,man/man{1,8}},var/log/httpd}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/apache

install -d $RPM_BUILD_ROOT%{_includedir}/apache

rm -f $RPM_BUILD_ROOT/etc/httpd/*
rm -f $RPM_BUILD_ROOT/home/httpd/html/manual/expand.pl

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,agent,referer}_log

cp -a apache-extra/errordocs	$RPM_BUILD_ROOT/home/httpd/
cp -a apache-extra/icons/*	$RPM_BUILD_ROOT/home/httpd/icons
cp -a apache-extra/*.conf	$RPM_BUILD_ROOT/etc/httpd
cp -a apache-extra/m*		$RPM_BUILD_ROOT/etc/httpd

mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_mandir}

strip $RPM_BUILD_ROOT/usr/lib/apache/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	ABOUT_APACHE src/CHANGES KEYS README README.v6

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add httpd
umask 137
touch /var/log/httpd/{access,error,agent,referer}_log
if [ -f /var/lock/subsys/httpd ]; then
   /etc/rc.d/init.d/httpd restart >&2
fi

%preun
if [ $1 = 0 ]; then
   if [ -f /var/lock/subsys/httpd ]; then
       /etc/rc.d/init.d/httpd stop >&2
   fi
   /sbin/chkconfig --del httpd
fi

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE.gz src/CHANGES.gz KEYS.gz README.gz
%doc conf/mime.types README.v6.gz

%attr(751,root,root) %dir /etc/httpd
%attr(640,root,root) %config %verify(not size mtime md5) /etc/httpd/*
%attr(640,root,root) %config %verify(not size mtime md5) /etc/sysconfig/*
%attr(640,root,root) %config /etc/logrotate.d/*

%attr(755,root,root) %dir /home/httpd/html

%config(noreplace) /home/httpd/html/index.html

%attr(644,root,root) /home/httpd/html/*.gif
%attr(755,root,root) /etc/rc.d/init.d/*

%attr(755,root,root) /home/httpd/cgi-bin
%attr(755,root,root) /usr/lib/apache

%attr(755,root,root) %dir /home/httpd/icons
/home/httpd/icons/*.gif

%attr(755,root,root) %dir /home/httpd/errordocs
/home/httpd/errordocs/*

%attr(755,root,root) %{_bindir}/dbmmanage 
%attr(755,root,root) %{_bindir}/htdigest
%attr(755,root,root) %{_bindir}/htpasswd

%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs

%dir %attr(750,http,http) /var/cache/www/apache

%{_mandir}/man[18]/*

%attr(750,root,root) %dir /var/log/httpd
%attr(640,root,root) %ghost /var/log/httpd/*

%files suexec
%attr(4711,root,root) %{_sbindir}/suexec

%files devel
%defattr(644,root,root,755) 

%dir %{_includedir}/apache
%{_includedir}/apache/*

%files doc
%defattr(644,root,root,755)
%attr(-,root,root) /home/httpd/html/manual

%changelog
* Wed May 26 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.6-2]
- misc changes for correct build,
- fixed apache.logrotate file,
- apache-htdosc.patch,
- added apache-release.patch,
- changed confdir to /etc/httpd instead /etc/httpd/conf,
- stripped modules & more changes,
- added new apache-extras packet,

  by Arek Mi¶kiewicz <misiek@pld.org.pl>
  
- added IPv6 support,
- other fixes.  


* Thu Feb 10 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [1.3.4-6d]
- added LDFLAGS=-s
- gzipping instead bzipping
- cosmetic changes

* Tue Jan 26 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.4-5d]
- rebuild against new kernel-2.2.0 ;)  

* Mon Jan 25 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.4-4d]
- added errordocs.  

* Thu Jan 21 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.4-3d]
- fixed files permission,
- fixed apache.init,
- some other changes.

* Sun Jan 17 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.4-2d]
- fixed sbindir && apache includes (by Mirek Nowakowski <nowam@pg.gda.pl>),
- compressed documentation,
- fixed Group(pl).

* Wed Nov 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3.3-1]
- removed making symlinks in /etc/rc.d/rc?.d and in %install also
  removed this symlinks from %files (/etc/rc.d/init.d/httpd suports
  chkconfig),
- more simplifications in %install,
- added new apache-config.patch,
- added "%ghost /var/log/httpd/suexec_log" for suexec subpackage,
- added "Requires: setup >= 1.10.0" for proper install in enviroment with
  http user/group.

* Wed Oct 14 1998 Konrad Stêpieñ <konrad@interdata.com.pl>
  [1.3.3-1d]
- up to 1.3.3
- changed user/group to http
- added patch against GNU libc-2.1, 
  prepared by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- enabled all modules (without auth_db ....)
- added magic (for mod_mime_magic)
- rebuild spec file to minimize number of patches
- suEXEC in separated package

* Wed Oct 14 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.2-1d]
- build against Tornado (GNU libc-2.1),
- minor changes. 

* Fri Sep 25 1998 Konrad Stêpieñ <konrad@interdata.com.pl>
  [1.3.2-1]
- up to 1.3.2
- reconfig to use /etc/mime.types (again)
  orginal mime.types can be found in documentation directory
- changed to user/group httpd
- restore orginal start page
- documentation in separate package
- added "Provides:httpd"

* Thu Sep  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3.1-2]
- removed /home/httpd/icons/README
- added devel subpackage,
- added pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>),
- removed Serial: filed,
- removed Packager: field (this must be placed in private ~/.rpmrc),
- simplification in %files and %install,
- /home/httpd/html/manual is now marked as %doc,
- added /etc/rc.d/rc*.d/* symlinks as a %config(missingok),
- changed permidssion on logrotate config file to 600,
- changed permidssion on /var/log/httpd to 700,
- added %ghost /var/log/httpd/*
- added striping modules,
- added patch to defeat header dos attack,
- start at spec file prepared by:
  Manoj Kasichainula <manojk@io.com>.

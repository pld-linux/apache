%include	/usr/lib/rpm/macros.perl
Summary:	The most widely used Web server on the Internet
Summary(de):	Leading World Wide Web-Server
Summary(fr):	Le serveur web le plus utilise sur Internet
Summary(pl):	Serwer WWW (World Wide Web)
Summary(tr):	Lider WWW tarayýcý
Name:		apache
Version:	1.3.11
Release:	4
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.apache.org/apache/dist/%{name}_%{version}.tar.gz
Source1:	apache.init
Source2:	apache.logrotate
Source3:	apache-icons.tar.gz
Source4:	apache.sysconfig
Source5:	apache-access.conf
Source6:	apache-httpd.conf
Source7:	apache-srm.conf
Source8:	apache-virtual-host.conf
Patch0:		apache-PLD.patch
Patch1:		apache-suexec.patch
Patch2:		apache-htdocs.patch
Patch7:		apache-errordocs.patch
Patch8:		apache-apxs.patch
Copyright:	BSD-like
Provides:	httpd
Provides:	webserver
Prereq:		/sbin/chkconfig
Prereq:		/usr/sbin/useradd
Prereq:		/usr/bin/getgid
Prereq:		/bin/id
Prereq:		sh-utils
#BuildRequires:	mm-devel
Requires:	rc-scripts
Requires:	mailcap
Requires:	/etc/mime.types
URL:		http://www.apache.org/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	apache-extra
Obsoletes:	apache6

%define		_sysconfdir	/etc/httpd
%define		_includedir	%{_prefix}/include/apache
%define		_datadir	/home/httpd
%define		_libexecdir	%{_prefix}/lib/apache

%description
Apache is a powerful, full-featured, efficient and freely-available Web
server. Apache is also the most popular Web server on the Internet.

%description -l de
Apache ist ein voll funktionsfähiger Web-Server, der kostenlos
erhältlich und weit verbreitet ist.

%description -l fr
Apache est un serveur Web puissant, efficace, gratuit et complet. Apache est
aussi le serveur Web le plus populaire sur Internet.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj±c ten pakiet bêdziesz 
móg³ prezentowaæ w³asne strony WWW w sieci internet.

%description -l tr
Apache serbest daðýtýlan ve çok kullanýlan yetenekli bir web sunucusudur.

%package suexec
Summary:	Apache suexec wrapper
Summary(pl):	Suexec wrapper do serwera www Apache
Group:		Networking/Development
Group(pl):	Sieciowe/Programowanie
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

%package devel
Summary:	Module development tools for the Apache web server
Summary(fr):	Les outils de developpement de modules pour le serveur web Apache
Summary(pl):	Pliki nag³ówkowe do tworzenai modu³ów rozszerzeñ do serwera www Apache
Group:		Networking/Development
Group(pl):	Sieciowe/Programowanie
Requires:	%{name} = %{version}

%description devel
The apache-devel package contains the source code for the Apache Web server
and the APXS binary you'll need to build Dynamic Shared Objects (DSOs) for
Apache.

%description -l fr devel
Le package apache-devel contient le code source pour le serveur Web Apache
et le binaire APXS dont vous aurez besoin pour construire des Objets
Dynamiques Partages (DSOs) pour Apache.

%description -l pl devel
Pliki nag³ówkowe dla serwera WWW Apache.

%package doc
Summary:	Apache dokumentation
Summary(pl):	Dokumentacja do Apache
Group:		Documentation
Group(pl):	Dokumentacja
Requires:	%{name} = %{version}
Obsoletes:	apache-manual

%description doc
Documentation for apache in HTML format.

%description -l pl doc
Dokumentacja do Apache w formacie HTML.

%prep 
%setup -q -n apache_%{version} -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch7 -p1
%patch8 -p1

%build

LDFLAGS="-s"
export LDFLAGS
OPTIM="$RPM_OPT_FLAGS" \
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--includedir=%{_includedir} \
	--sbindir=%{_sbindir} \
	--libexecdir=%{_libexecdir} \
	--datadir=%{_datadir} \
	--localstatedir=/var \
	--runtimedir=/var/run \
	--logfiledir=/var/log/httpd \
	--with-layout=PLD \
	--without-confadjust \
	--enable-module=all \
	--enable-shared=max \
	--proxycachedir=/var/cache/www/apache \
	--with-perl=%{_bindir}/perl \
	--enable-suexec \
	--suexec-caller=http \
	--suexec-uidmin=500 \
	--suexec-gidmin=500 \
	--disable-rule=WANTHSREGEX
make

%install
rm -rf $RPM_BUILD_ROOT

make install-quiet root="$RPM_BUILD_ROOT"

#mv $RPM_BUILD_ROOT%{_datadir}/htdocs $RPM_BUILD_ROOT%{_datadir}/html

install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT%{_datadir}/errordocs \
	$RPM_BUILD_ROOT/var/{log/{httpd,archiv/httpd},state/apache/mm}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/apache

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/*

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,agent,referer}_log

install errordocs/* $RPM_BUILD_ROOT%{_datadir}/errordocs

install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/access.conf
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/srm.conf
install %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/virtual-host.conf

ln -sf index.html.en $RPM_BUILD_ROOT/home/httpd/html/index.html

strip --strip-unneeded $RPM_BUILD_ROOT%{_libexecdir}/*.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	ABOUT_APACHE src/CHANGES KEYS README

%pre
if [ -n "`getgid http`" ]; then
	if [ "`getgid http`" != "51" ]; then
		echo "Warning: group http haven't gid=51. Corect this before install apache" 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 51 -r -f http
	if [ -f /var/db/group.db ]; then
		/usr/bin/update-db 1>&2
	fi
fi
if [ -n "`id -u http 2>/dev/null`" ]; then
	if [ "`id -u http`" != "51" ]; then
		echo "Warning: user http haven't uid=51. Corect this before install apache" 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 51 -r -d /home/httpd -s /bin/false -c "HTTP User" -g http http 1>&2
	if [ -f /var/db/passwd.db ]; then
		/usr/bin/update-db 1>&2
	fi
fi


%post
/sbin/chkconfig --add httpd
umask 137
touch /var/log/httpd/{access,error,agent,referer}_log
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd stop 1>&2
	fi
	/sbin/chkconfig --del httpd
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/userdel http
	if [ -f /var/db/passwd.db ]; then
		/usr/bin/update-db
	fi
	/usr/sbin/groupdel http
	if [ -f /var/db/group.db ]; then
		/usr/bin/update-db
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE.gz src/CHANGES.gz KEYS.gz README.gz
%doc conf/mime.types

%attr(754,root,root) /etc/rc.d/init.d/httpd

%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/*
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/*

%attr(755,root,root) %dir %{_datadir}/html
%config(noreplace) %{_datadir}/html/index.html
%lang(ca) %{_datadir}/html/index.html.ca
%lang(cz) %{_datadir}/html/index.html.cz
%lang(de) %{_datadir}/html/index.html.de
%lang(dk) %{_datadir}/html/index.html.dk
%lang(ee) %{_datadir}/html/index.html.ee
%lang(en) %{_datadir}/html/index.html.en
%lang(es) %{_datadir}/html/index.html.es
%lang(fr) %{_datadir}/html/index.html.fr
%lang(it) %{_datadir}/html/index.html.it
%lang(lu) %{_datadir}/html/index.html.lu
%lang(nl) %{_datadir}/html/index.html.nl
%lang(pt) %{_datadir}/html/index.html.pt
%lang(se) %{_datadir}/html/index.html.se

%{_datadir}/html/*.gif
%{_datadir}/errordocs
%dir %{_datadir}/icons
%{_datadir}/icons/*.gif
%dir %{_datadir}/icons/small
%{_datadir}/icons/small/*.gif
%attr(755,root,root) %{_datadir}/cgi-bin

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/*

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

%dir %attr(750,http,http) /var/state/apache

%{_mandir}/man[18]/*

%attr(750,root,root) %dir /var/log/httpd
%attr(750,root,root) %dir /var/log/archiv/httpd
%attr(640,root,root) %ghost /var/log/httpd/*

%files suexec
%attr(4755,root,root) %{_sbindir}/suexec

%files devel
%defattr(644,root,root,755) 

%{_includedir}

%files doc
%defattr(644,root,root,755)
%attr(-,root,root) %{_datadir}/html/manual

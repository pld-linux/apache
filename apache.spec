%include	/usr/lib/rpm/macros.perl
Summary:	The most widely used Web server on the Internet
Summary(de):	Leading World Wide Web-Server
Summary(fr):	Le serveur web le plus utilise sur Internet
Summary(pl):	Serwer WWW (World Wide Web)
Summary(tr):	Lider WWW tarayýcý
Name:		apache
Version:	1.3.11
Release:	5
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

%package mod_proxy
Summary:	Apache Web proxy module
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:
Requires:	%{name} = %{version}

%description mod_proxy
This module implements a proxy/cache for Apache. It implements proxying
capability for FTP, CONNECT (for SSL), HTTP/0.9, and HTTP/1.0. The module
can be configured to connect to other proxy modules for these and other
protocols.

%package mod_vhost_alias
Summary:	Apache dynamically configured mass virtual hosting module
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:
Requires:	%{name} = %{version}

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

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
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi
/usr/sbin/apxs -e -a -n mod_access %{_libexecdir}/mod_access.so 1>&2
/usr/sbin/apxs -e -a -n mod_actions %{_libexecdir}/mod_actions.so 1>&2
/usr/sbin/apxs -e -a -n mod_alias %{_libexecdir}/mod_alias.so 1>&2
/usr/sbin/apxs -e -a -n mod_asis %{_libexecdir}/mod_asis.so 1>&2
/usr/sbin/apxs -e -a -n mod_auth %{_libexecdir}/mod_auth.so 1>&2
/usr/sbin/apxs -e -a -n mod_auth_anon %{_libexecdir}/mod_auth_anon.so 1>&2
/usr/sbin/apxs -e -a -n mod_auth_db %{_libexecdir}/mod_auth_db.so 1>&2
/usr/sbin/apxs -e -a -n mod_auth_dbm %{_libexecdir}/mod_auth_dbm.so 1>&2
/usr/sbin/apxs -e -a -n mod_autoindex %{_libexecdir}/mod_autoindex.so 1>&2
/usr/sbin/apxs -e -a -n mod_cern_meta %{_libexecdir}/mod_cern_meta.so 1>&2
/usr/sbin/apxs -e -a -n mod_cgi %{_libexecdir}/mod_cgi.so 1>&2
/usr/sbin/apxs -e -a -n mod_digest %{_libexecdir}/mod_digest.so 1>&2
/usr/sbin/apxs -e -a -n mod_dir %{_libexecdir}/mod_dir.so 1>&2
/usr/sbin/apxs -e -a -n mod_env %{_libexecdir}/mod_env.so 1>&2
/usr/sbin/apxs -e -a -n mod_example %{_libexecdir}/mod_example.so 1>&2
/usr/sbin/apxs -e -a -n mod_expires %{_libexecdir}/mod_expires.so 1>&2
/usr/sbin/apxs -e -a -n mod_headers %{_libexecdir}/mod_headers.so 1>&2
/usr/sbin/apxs -e -a -n mod_imap %{_libexecdir}/mod_imap.so 1>&2
/usr/sbin/apxs -e -a -n mod_include %{_libexecdir}/mod_include.so 1>&2
/usr/sbin/apxs -e -a -n mod_info %{_libexecdir}/mod_info.so 1>&2
/usr/sbin/apxs -e -a -n mod_log_agent %{_libexecdir}/mod_log_agent.so 1>&2
/usr/sbin/apxs -e -a -n mod_log_config %{_libexecdir}/mod_log_config.so 1>&2
/usr/sbin/apxs -e -a -n mod_log_referer %{_libexecdir}/mod_log_referer.so 1>&2
/usr/sbin/apxs -e -a -n mod_mime %{_libexecdir}/mod_mime.so 1>&2
/usr/sbin/apxs -e -a -n mod_mime_magic %{_libexecdir}/mod_mime_magic.so 1>&2
/usr/sbin/apxs -e -a -n mod_mmap_static %{_libexecdir}/mod_mmap_static.so 1>&2
/usr/sbin/apxs -e -a -n mod_negotiation %{_libexecdir}/mod_negotiation.so 1>&2
/usr/sbin/apxs -e -a -n mod_rewrite %{_libexecdir}/mod_rewrite.so 1>&2
/usr/sbin/apxs -e -a -n mod_setenvif %{_libexecdir}/mod_setenvif.so 1>&2
/usr/sbin/apxs -e -a -n mod_speling %{_libexecdir}/mod_speling.so 1>&2
/usr/sbin/apxs -e -a -n mod_status %{_libexecdir}/mod_status.so 1>&2
/usr/sbin/apxs -e -a -n mod_unique_id %{_libexecdir}/mod_unique_id.so 1>&2
/usr/sbin/apxs -e -a -n mod_userdir %{_libexecdir}/mod_userdir.so 1>&2
/usr/sbin/apxs -e -a -n mod_usertrack %{_libexecdir}/mod_usertrack.so 1>&2
/usr/sbin/apxs -e -a -n mod_vhost_alias %{_libexecdir}/mod_vhost_alias.so 1>&2

%preun
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n mod_access %{_libexecdir}/mod_access.so 1>&2
	/usr/sbin/apxs -e -A -n mod_actions %{_libexecdir}/mod_actions.so 1>&2
	/usr/sbin/apxs -e -A -n mod_alias %{_libexecdir}/mod_alias.so 1>&2
	/usr/sbin/apxs -e -A -n mod_asis %{_libexecdir}/mod_asis.so 1>&2
	/usr/sbin/apxs -e -A -n mod_auth %{_libexecdir}/mod_auth.so 1>&2
	/usr/sbin/apxs -e -A -n mod_auth_anon %{_libexecdir}/mod_auth_anon.so 1>&2
	/usr/sbin/apxs -e -A -n mod_auth_db %{_libexecdir}/mod_auth_db.so 1>&2
	/usr/sbin/apxs -e -A -n mod_auth_dbm %{_libexecdir}/mod_auth_dbm.so 1>&2
	/usr/sbin/apxs -e -A -n mod_autoindex %{_libexecdir}/mod_autoindex.so 1>&2
	/usr/sbin/apxs -e -A -n mod_cern_meta %{_libexecdir}/mod_cern_meta.so 1>&2
	/usr/sbin/apxs -e -A -n mod_cgi %{_libexecdir}/mod_cgi.so 1>&2
	/usr/sbin/apxs -e -A -n mod_digest %{_libexecdir}/mod_digest.so 1>&2
	/usr/sbin/apxs -e -A -n mod_dir %{_libexecdir}/mod_dir.so 1>&2
	/usr/sbin/apxs -e -A -n mod_env %{_libexecdir}/mod_env.so 1>&2
	/usr/sbin/apxs -e -A -n mod_example %{_libexecdir}/mod_example.so 1>&2
	/usr/sbin/apxs -e -A -n mod_expires %{_libexecdir}/mod_expires.so 1>&2
	/usr/sbin/apxs -e -A -n mod_headers %{_libexecdir}/mod_headers.so 1>&2
	/usr/sbin/apxs -e -A -n mod_imap %{_libexecdir}/mod_imap.so 1>&2
	/usr/sbin/apxs -e -A -n mod_include %{_libexecdir}/mod_include.so 1>&2
	/usr/sbin/apxs -e -A -n mod_info %{_libexecdir}/mod_info.so 1>&2
	/usr/sbin/apxs -e -A -n mod_log_agent %{_libexecdir}/mod_log_agent.so 1>&2
	/usr/sbin/apxs -e -A -n mod_log_config %{_libexecdir}/mod_log_config.so 1>&2
	/usr/sbin/apxs -e -A -n mod_log_referer %{_libexecdir}/mod_log_referer.so 1>&2
	/usr/sbin/apxs -e -A -n mod_mime %{_libexecdir}/mod_mime.so 1>&2
	/usr/sbin/apxs -e -A -n mod_mime_magic %{_libexecdir}/mod_mime_magic.so 1>&2
	/usr/sbin/apxs -e -A -n mod_mmap_static %{_libexecdir}/mod_mmap_static.so 1>&2
	/usr/sbin/apxs -e -A -n mod_negotiation %{_libexecdir}/mod_negotiation.so 1>&2
	/usr/sbin/apxs -e -A -n mod_rewrite %{_libexecdir}/mod_rewrite.so 1>&2
	/usr/sbin/apxs -e -A -n mod_setenvif %{_libexecdir}/mod_setenvif.so 1>&2
	/usr/sbin/apxs -e -A -n mod_speling %{_libexecdir}/mod_speling.so 1>&2
	/usr/sbin/apxs -e -A -n mod_status %{_libexecdir}/mod_status.so 1>&2
	/usr/sbin/apxs -e -A -n mod_unique_id %{_libexecdir}/mod_unique_id.so 1>&2
	/usr/sbin/apxs -e -A -n mod_userdir %{_libexecdir}/mod_userdir.so 1>&2
	/usr/sbin/apxs -e -A -n mod_usertrack %{_libexecdir}/mod_usertrack.so 1>&2
	/usr/sbin/apxs -e -A -n mod_vhost_alias %{_libexecdir}/mod_vhost_alias.so 1>&2
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

%post mod_proxy
/usr/sbin/apxs -e -a -n libproxy %{_libexecdir}/libproxy.so 1>&2

%preun mod_proxy
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n libproxy %{_libexecdir}/libproxy.so 1>&2
fi

%post mod_vhost_alias
/usr/sbin/apxs -e -a -n libproxy %{_libexecdir}/mod_vhost_alias.so 1>&2

%preun mod_vhost_alias
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n libproxy %{_libexecdir}/mod_vhost_alias.so 1>&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE.gz src/CHANGES.gz KEYS.gz README.gz
%doc conf/mime.types

%attr(754,root,root) /etc/rc.d/init.d/httpd

%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/access.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/srm.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/virtual-host.conf
%attr(640,root,root) %{_sysconfdir}/magic

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
%attr(755,root,root) %{_libexecdir}/mod_access.so
%attr(755,root,root) %{_libexecdir}/mod_actions.so
%attr(755,root,root) %{_libexecdir}/mod_alias.so
%attr(755,root,root) %{_libexecdir}/mod_asis.so
%attr(755,root,root) %{_libexecdir}/mod_auth.so
%attr(755,root,root) %{_libexecdir}/mod_auth_anon.so
%attr(755,root,root) %{_libexecdir}/mod_auth_db.so
%attr(755,root,root) %{_libexecdir}/mod_auth_dbm.so
%attr(755,root,root) %{_libexecdir}/mod_autoindex.so
%attr(755,root,root) %{_libexecdir}/mod_cern_meta.so
%attr(755,root,root) %{_libexecdir}/mod_cgi.so
%attr(755,root,root) %{_libexecdir}/mod_digest.so
%attr(755,root,root) %{_libexecdir}/mod_dir.so
%attr(755,root,root) %{_libexecdir}/mod_env.so
%attr(755,root,root) %{_libexecdir}/mod_example.so
%attr(755,root,root) %{_libexecdir}/mod_expires.so
%attr(755,root,root) %{_libexecdir}/mod_headers.so
%attr(755,root,root) %{_libexecdir}/mod_imap.so
%attr(755,root,root) %{_libexecdir}/mod_include.so
%attr(755,root,root) %{_libexecdir}/mod_info.so
%attr(755,root,root) %{_libexecdir}/mod_log_agent.so
%attr(755,root,root) %{_libexecdir}/mod_log_config.so
%attr(755,root,root) %{_libexecdir}/mod_log_referer.so
%attr(755,root,root) %{_libexecdir}/mod_mime.so
%attr(755,root,root) %{_libexecdir}/mod_mime_magic.so
%attr(755,root,root) %{_libexecdir}/mod_mmap_static.so
%attr(755,root,root) %{_libexecdir}/mod_negotiation.so
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so
%attr(755,root,root) %{_libexecdir}/mod_setenvif.so
%attr(755,root,root) %{_libexecdir}/mod_speling.so
%attr(755,root,root) %{_libexecdir}/mod_status.so
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so
%attr(755,root,root) %{_libexecdir}/mod_userdir.so
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so

%attr(755,root,root) %{_bindir}/dbmmanage 
%attr(755,root,root) %{_bindir}/htdigest
%attr(755,root,root) %{_bindir}/htpasswd

%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs

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
%dir %{_datadir}/html/manual/
%{_datadir}/html/manual/images
%{_datadir}/html/manual/misc
%dir %{_datadir}/html/manual/serach
%attr(755,root,root) %{_datadir}/html/manual/serach/manual-index.cgi
%{_datadir}/html/manual/vhosts
%{_datadir}/html/manual/LICENSE
%{_datadir}/html/manual/*.html
%{_datadir}/html/manual/mod/core.html
%{_datadir}/html/manual/mod/directive-dict.html
%{_datadir}/html/manual/mod/directives.html
%{_datadir}/html/manual/mod/footer.html
%{_datadir}/html/manual/mod/header.html
%{_datadir}/html/manual/mod/index.html
%{_datadir}/html/manual/mod/mod_access.html
%{_datadir}/html/manual/mod/mod_actions.html
%{_datadir}/html/manual/mod/mod_alias.html
%{_datadir}/html/manual/mod/mod_asis.html
%{_datadir}/html/manual/mod/mod_auth.html
%{_datadir}/html/manual/mod/mod_auth_anon.html
%{_datadir}/html/manual/mod/mod_auth_db.html
%{_datadir}/html/manual/mod/mod_auth_dbm.html
%{_datadir}/html/manual/mod/mod_autoindex.html
%{_datadir}/html/manual/mod/mod_cgi.html
%{_datadir}/html/manual/mod/mod_cookies.html
%{_datadir}/html/manual/mod/mod_digest.html
%{_datadir}/html/manual/mod/mod_dir.html
%{_datadir}/html/manual/mod/mod_env.html
%{_datadir}/html/manual/mod/mod_example.html
%{_datadir}/html/manual/mod/mod_expires.html
%{_datadir}/html/manual/mod/mod_headers.html
%{_datadir}/html/manual/mod/mod_imap.html
%{_datadir}/html/manual/mod/mod_include.html
%{_datadir}/html/manual/mod/mod_info.html
%{_datadir}/html/manual/mod/mod_log_agent.html
%{_datadir}/html/manual/mod/mod_log_config.html
%{_datadir}/html/manual/mod/mod_log_referer.html
%{_datadir}/html/manual/mod/mod_mime.html
%{_datadir}/html/manual/mod/mod_mime_magic.html
%{_datadir}/html/manual/mod/mod_mmap_static.html
%{_datadir}/html/manual/mod/mod_negotiation.html
%{_datadir}/html/manual/mod/mod_rewrite.html
%{_datadir}/html/manual/mod/mod_setenvif.html
%{_datadir}/html/manual/mod/mod_so.html
%{_datadir}/html/manual/mod/mod_speling.html
%{_datadir}/html/manual/mod/mod_status.html
%{_datadir}/html/manual/mod/mod_unique_id.html
%{_datadir}/html/manual/mod/mod_userdir.html
%{_datadir}/html/manual/mod/mod_usertrack.html

%package mod_proxy
%attr(755,root,root) %{_libexecdir}/libproxy.so
%attr(644,root,root) %{_datadir}/html/manual/mod/mod_proxy.html
%dir %attr(750,http,http) /var/cache/www/apache

%package mod_vhost_alias
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
%attr(644,root,root) %{_datadir}/html/manual/mod/mod_vhost_alias.html

%include	/usr/lib/rpm/macros.perl
Summary:	The most widely used Web server on the Internet
Summary(de):	Leading World Wide Web-Server
Summary(fr):	Le serveur web le plus utilise sur Internet
Summary(pl):	Serwer WWW (World Wide Web)
Summary(tr):	Lider WWW tarayýcý
Name:		apache
Version:	1.3.12
Release:	1
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.apache.org/dist/%{name}_%{version}.tar.gz
Source1:	apache.init
Source2:	apache.logrotate
Source3:	apache-icons.tar.gz
Source4:	apache.sysconfig
Source5:	apache-access.conf
Source6:	apache-httpd.conf
Source7:	apache-srm.conf
Source8:	apache-virtual-host.conf
Source9:	apache-mod_status.conf
Patch0:		apache-PLD.patch
Patch1:		apache-suexec.patch
Patch2:		apache-htdocs.patch
Patch3:		apache-errordocs.patch
Patch4:		apache-apxs.patch
Patch5:		apache-EAPI.patch
Patch6:		apache-v6-PLD-1.patch.gz
Copyright:	BSD-like
Provides:	httpd
Provides:	webserver
Prereq:		/sbin/chkconfig
Prereq:		/usr/sbin/useradd
Prereq:		/usr/bin/getgid
Prereq:		/bin/id
Prereq:		sh-utils
BuildRequires:	mm-devel
Requires:	rc-scripts
Requires:	mailcap
Requires:	/etc/mime.types
URL:		http://www.apache.org/
BuildRoot:	/tmp/%{name}-%{version}-root
Provides:	apache(EAPI)
Obsoletes:	apache-extra
Obsoletes:	apache6
Obsoletes:	apache-doc

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
Requires:	%{name}(EAPI) = %{version}

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
Requires:	%{name}(EAPI) = %{version}
Provides:	%{name}(EAPI)-devel

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

%package mod_actions
Summary:	Apache module for run CGI whenever a file of a certain type is requested
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_actions
This package contains mod_actions module. This module lets you run CGI
scripts whenever a file of a certain type is requested. This makes it much
easier to execute scripts that process files.

%package mod_auth_anon
Summary:	Apache module with "anonymous" user access authentication
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_auth_anon
This package contains mod_auth_anon module. It allows "anonymous" user
access to authenticated areas. It does access control in a manner similar to
anonymous-ftp sites; i.e. have a 'magic' user id 'anonymous' and the email
address as a password. These email addresses can be logged. Combined with
other (database) access control methods, this allows for effective user
tracking and customization according to a user profile while still keeping
the site open for 'unregistered' users. One advantage of using Auth-based
user tracking is that, unlike magic-cookies and funny URL pre/postfixes, it
is completely browser independent and it allows users to share URLs.

%package mod_define
Summary:	Apache module - authentication variables for arbitrary directives
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_define
It provides the definition variables for arbitrary directives, i.e.
variables which can be expanded on any(!) directive line.

%package mod_digest
Summary:	Apache user authentication module using MD5 Digest Authentication 
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_digest
This package contains mod_dir module. It provides user authentication using
MD5 Digest Authentication.

%package mod_dir
Summary:	Apache module for trailing slash" redirects and serving directory index files
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_dir
This package contains mod_dir which provides "trailing slash" redirects and
serving directory index files.

%package mod_headers
Summary:	Apache module allows for the customization of HTTP response headers
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_headers
This package contains mod_headers module. The module allows for the
customization of HTTP response headers. Headers can be merged, replaced or
removed.

%package mod_mmap_static
Summary:	Apache module for mmap()ing statically configured list files
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_mmap_static
This package contains mod_mmap_static module. It provides mmap()ing of a
statically configured list of frequently requested but not changed files.

%package mod_imap
Summary:	Apache module with imap-file handler
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_imap
This package contains mod_imap module. It provides for .map files, replacing
the functionality of the imagemap CGI program. Any directory or document
type configured to use the handler imap-file.

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_info
This package contains mod_mmap_static module. It provides a comprehensive
overview of the server configuration including all installed modules and
directives in the configuration files.

%package mod_proxy
Summary:	Apache module with Web proxy
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_proxy
This package contains module with implementation a proxy/cache for Apache.
It implements proxying capability for FTP, CONNECT (for SSL), HTTP/0.9, and
HTTP/1.0. The module can be configured to connect to other proxy modules for
these and other protocols.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to rewrite
requested URLs on the fly.

%package mod_status
Summary:	Server status report module for apache
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_status
The Status module allows a server administrator to find out how well their
server is performing. A HTML page is presented that gives the current server
statistics in an easily readable form. If required this page can be made to
automatically refresh (given a compatible browser).

%package mod_usertrack
Summary:	Apache module for user tracking using cookies
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_usertrack
This package contains the user tracking module which did its own logging
using CookieLog directory. This module allow multiple log files.

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

%package mod_unique_id
Summary:	Apache module which provides a magic token for each request
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_unique_id
This package contains the mod_unique_id. This module provides a magic token
for each request which is guaranteed to be unique across "all" requests
under very specific conditions. The unique identifier is even unique across
multiple machines in a properly configured cluster of machines. The
environment variable UNIQUE_ID is set to the identifier for each request.
Unique identifiers are useful for various reasons which are beyond the scope
of this document.

%package mod_expires
Summary:	Apache module which provides .... 
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		%{_sbindir}/apxs
Requires:	%{name}(EAPI) = %{version}

%description mod_expires

%prep 
%setup -q -n apache_%{version} -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1

%build

LDFLAGS="-s"; export LDFLAGS
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
	--proxycachedir=/var/cache/apache \
	--with-perl=%{_bindir}/perl \
	--enable-suexec \
	--suexec-caller=http \
	--suexec-uidmin=500 \
	--suexec-gidmin=500 \
	--disable-rule=WANTHSREGEX \
	--enable-rule=EAPI
#	--enable-rule=INET6
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT%{_datadir}/errordocs \
	$RPM_BUILD_ROOT/var/{log/{httpd,archiv/httpd},state/apache/mm}

make install-quiet root="$RPM_BUILD_ROOT"

mv $RPM_BUILD_ROOT%{_datadir}/html/manual $RPM_BUILD_ROOT%{_datadir}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/apache

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
%{_sbindir}/apxs -e -a -n access %{_libexecdir}/mod_access.so 1>&2
%{_sbindir}/apxs -e -a -n alias %{_libexecdir}/mod_alias.so 1>&2
%{_sbindir}/apxs -e -a -n asis %{_libexecdir}/mod_asis.so 1>&2
%{_sbindir}/apxs -e -a -n auth %{_libexecdir}/mod_auth.so 1>&2
%{_sbindir}/apxs -e -a -n db_auth %{_libexecdir}/mod_auth_db.so 1>&2
%{_sbindir}/apxs -e -a -n dbm_auth %{_libexecdir}/mod_auth_dbm.so 1>&2
%{_sbindir}/apxs -e -a -n autoindex %{_libexecdir}/mod_autoindex.so 1>&2
%{_sbindir}/apxs -e -a -n cern_meta %{_libexecdir}/mod_cern_meta.so 1>&2
%{_sbindir}/apxs -e -a -n cgi %{_libexecdir}/mod_cgi.so 1>&2
%{_sbindir}/apxs -e -a -n env %{_libexecdir}/mod_env.so 1>&2
%{_sbindir}/apxs -e -a -n includes %{_libexecdir}/mod_include.so 1>&2
%{_sbindir}/apxs -e -a -n agent_log %{_libexecdir}/mod_log_agent.so 1>&2
%{_sbindir}/apxs -e -a -n config_log %{_libexecdir}/mod_log_config.so 1>&2
%{_sbindir}/apxs -e -a -n referer_log %{_libexecdir}/mod_log_referer.so 1>&2
%{_sbindir}/apxs -e -a -n mime %{_libexecdir}/mod_mime.so 1>&2
%{_sbindir}/apxs -e -a -n mime_magic %{_libexecdir}/mod_mime_magic.so 1>&2
%{_sbindir}/apxs -e -a -n negotiation %{_libexecdir}/mod_negotiation.so 1>&2
%{_sbindir}/apxs -e -a -n setenvif %{_libexecdir}/mod_setenvif.so 1>&2
%{_sbindir}/apxs -e -a -n speling %{_libexecdir}/mod_speling.so 1>&2
%{_sbindir}/apxs -e -a -n userdir %{_libexecdir}/mod_userdir.so 1>&2
umask 137
touch /var/log/httpd/{access,error,agent,referer}_log
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n access %{_libexecdir}/mod_access.so 1>&2
	%{_sbindir}/apxs -e -A -n alias %{_libexecdir}/mod_alias.so 1>&2
	%{_sbindir}/apxs -e -A -n asis %{_libexecdir}/mod_asis.so 1>&2
	%{_sbindir}/apxs -e -A -n auth %{_libexecdir}/mod_auth.so 1>&2
	%{_sbindir}/apxs -e -A -n db_auth %{_libexecdir}/mod_auth_db.so 1>&2
	%{_sbindir}/apxs -e -A -n dbm_auth %{_libexecdir}/mod_auth_dbm.so 1>&2
	%{_sbindir}/apxs -e -A -n autoindex %{_libexecdir}/mod_autoindex.so 1>&2
	%{_sbindir}/apxs -e -A -n cern_meta %{_libexecdir}/mod_cern_meta.so 1>&2
	%{_sbindir}/apxs -e -A -n cgi %{_libexecdir}/mod_cgi.so 1>&2
	%{_sbindir}/apxs -e -A -n env %{_libexecdir}/mod_env.so 1>&2
	%{_sbindir}/apxs -e -A -n includes %{_libexecdir}/mod_include.so 1>&2
	%{_sbindir}/apxs -e -A -n agent_log %{_libexecdir}/mod_log_agent.so 1>&2
	%{_sbindir}/apxs -e -A -n config_log %{_libexecdir}/mod_log_config.so 1>&2
	%{_sbindir}/apxs -e -A -n referer_log %{_libexecdir}/mod_log_referer.so 1>&2
	%{_sbindir}/apxs -e -A -n mime %{_libexecdir}/mod_mime.so 1>&2
	%{_sbindir}/apxs -e -A -n mime_magic %{_libexecdir}/mod_mime_magic.so 1>&2
	%{_sbindir}/apxs -e -A -n negotiation %{_libexecdir}/mod_negotiation.so 1>&2
	%{_sbindir}/apxs -e -A -n setenvif %{_libexecdir}/mod_setenvif.so 1>&2
	%{_sbindir}/apxs -e -A -n speling %{_libexecdir}/mod_speling.so 1>&2
	%{_sbindir}/apxs -e -A -n userdir %{_libexecdir}/mod_userdir.so 1>&2
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

%post mod_actions
%{_sbindir}/apxs -e -a -n action %{_libexecdir}/mod_actions.so 1>&2

%preun mod_actions
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n action %{_libexecdir}/mod_actions.so 1>&2
fi

%post mod_auth_anon
%{_sbindir}/apxs -e -a -n anon_auth %{_libexecdir}/mod_auth_anon.so 1>&2

%preun mod_auth_anon
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n anon_auth %{_libexecdir}/mod_auth_anon.so 1>&2
fi

%post mod_define
%{_sbindir}/apxs -e -a -n digest %{_libexecdir}/mod_define.so 1>&2

%preun mod_define
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n digest %{_libexecdir}/mod_define.so 1>&2
fi

%post mod_digest
%{_sbindir}/apxs -e -a -n digest %{_libexecdir}/mod_digest.so 1>&2

%preun mod_digest
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n digest %{_libexecdir}/mod_digest.so 1>&2
fi

%post mod_dir
%{_sbindir}/apxs -e -a -n dir %{_libexecdir}/mod_dir.so 1>&2

%preun mod_dir
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n dir %{_libexecdir}/mod_dir.so 1>&2
fi

%post mod_expires
%{_sbindir}/apxs -e -a -n expires %{_libexecdir}/mod_expires.so 1>&2

%preun mod_expires
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n expires %{_libexecdir}/mod_expires.so 1>&2
fi

%post mod_headers
%{_sbindir}/apxs -e -a -n headers %{_libexecdir}/mod_headers.so 1>&2

%preun mod_headers
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n headers %{_libexecdir}/mod_headers.so 1>&2
fi

%post mod_mmap_static
%{_sbindir}/apxs -e -a -n mmap_static %{_libexecdir}/mod_mmap_static.so 1>&2

%preun mod_mmap_static
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n mmap_static %{_libexecdir}/mod_mmap_static.so 1>&2
fi

%post mod_imap
%{_sbindir}/apxs -e -a -n imap %{_libexecdir}/mod_imap.so 1>&2

%preun mod_imap
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n imap %{_libexecdir}/mod_imap.so 1>&2
fi

%post mod_info
%{_sbindir}/apxs -e -a -n info %{_libexecdir}/mod_info.so 1>&2

%preun mod_info
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n info %{_libexecdir}/mod_info.so 1>&2
fi

%post mod_proxy
%{_sbindir}/apxs -e -a -n proxy %{_libexecdir}/libproxy.so 1>&2

%preun mod_proxy
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n proxy %{_libexecdir}/libproxy.so 1>&2
fi

%post mod_rewrite
%{_sbindir}/apxs -e -a -n rewrite %{_libexecdir}/mod_rewrite.so 1>&2

%preun mod_rewrite
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n rewrite %{_libexecdir}/mod_rewrite.so 1>&2
fi

%post mod_status
%{_sbindir}/apxs -e -a -n status %{_libexecdir}/mod_status.so 1>&2

%preun mod_status
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n status %{_libexecdir}/mod_status.so 1>&2
fi

%post mod_usertrack
%{_sbindir}/apxs -e -a -n usertrack %{_libexecdir}/mod_usertrack.so 1>&2

%preun mod_usertrack
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n usertrack %{_libexecdir}/mod_usertrack.so 1>&2
fi

%post mod_unique_id
%{_sbindir}/apxs -e -a -n unique_id %{_libexecdir}/mod_unique_id.so 1>&2

%preun mod_unique_id
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n unique_id %{_libexecdir}/mod_unique_id.so 1>&2
fi

%post mod_vhost_alias
%{_sbindir}/apxs -e -a -n vhost_alias %{_libexecdir}/mod_vhost_alias.so 1>&2

%preun mod_vhost_alias
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n vhost_alias %{_libexecdir}/mod_vhost_alias.so 1>&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE.gz src/CHANGES.gz KEYS.gz README.gz
%doc conf/mime.types

%dir %{_datadir}/manual
%dir %{_datadir}/manual/images/
%{_datadir}/manual/images/sub.gif
%{_datadir}/manual/images/index.gif
%{_datadir}/manual/images/home.gif 
%{_datadir}/manual/misc
%dir %{_datadir}/manual/search
%attr(755,root,root) %{_datadir}/manual/search/manual-index.cgi
%{_datadir}/manual/vhosts
%{_datadir}/manual/LICENSE
%{_datadir}/manual/bind.html
%{_datadir}/manual/cgi_path.html
%{_datadir}/manual/content-negotiation.html
%{_datadir}/manual/custom-error.html
%{_datadir}/manual/dns-caveats.html
%{_datadir}/manual/dso.html
%{_datadir}/manual/env.html
%{_datadir}/manual/footer.html
%{_datadir}/manual/handler.html
%{_datadir}/manual/header.html
%{_datadir}/manual/index.html
%{_datadir}/manual/install.html
%{_datadir}/manual/invoking.html
%{_datadir}/manual/keepalive.html
%{_datadir}/manual/location.html
%{_datadir}/manual/multilogs.html
%{_datadir}/manual/new_features_1_3.html
%{_datadir}/manual/process-model.html
%{_datadir}/manual/sections.html
%{_datadir}/manual/sourcereorg.html
%{_datadir}/manual/suexec.html
%{_datadir}/manual/upgrading_to_1_3.html
%{_datadir}/manual/mod/core.html
%{_datadir}/manual/mod/directive-dict.html
%{_datadir}/manual/mod/directives.html
%{_datadir}/manual/mod/footer.html
%{_datadir}/manual/mod/header.html
%{_datadir}/manual/mod/index.html
%{_datadir}/manual/mod/mod_access.html
%{_datadir}/manual/mod/mod_alias.html
%{_datadir}/manual/mod/mod_asis.html
%{_datadir}/manual/mod/mod_auth.html
%{_datadir}/manual/mod/mod_auth_db.html
%{_datadir}/manual/mod/mod_auth_dbm.html
%{_datadir}/manual/mod/mod_autoindex.html
%{_datadir}/manual/mod/mod_cgi.html
%{_datadir}/manual/mod/mod_cookies.html
%{_datadir}/manual/mod/mod_env.html
%{_datadir}/manual/mod/mod_include.html
%{_datadir}/manual/mod/mod_log_agent.html
%{_datadir}/manual/mod/mod_log_config.html
%{_datadir}/manual/mod/mod_log_referer.html
%{_datadir}/manual/mod/mod_mime.html
%{_datadir}/manual/mod/mod_mime_magic.html
%{_datadir}/manual/mod/mod_negotiation.html
%{_datadir}/manual/mod/mod_setenvif.html
%{_datadir}/manual/mod/mod_speling.html
%{_datadir}/manual/mod/mod_userdir.html

%attr(754,root,root) /etc/rc.d/init.d/httpd

%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/access.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/srm.conf
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
%attr(755,root,root) %{_libexecdir}/mod_alias.so
%attr(755,root,root) %{_libexecdir}/mod_asis.so
%attr(755,root,root) %{_libexecdir}/mod_auth.so
%attr(755,root,root) %{_libexecdir}/mod_auth_db.so
%attr(755,root,root) %{_libexecdir}/mod_auth_dbm.so
%attr(755,root,root) %{_libexecdir}/mod_autoindex.so
%attr(755,root,root) %{_libexecdir}/mod_cern_meta.so
%attr(755,root,root) %{_libexecdir}/mod_cgi.so
%attr(755,root,root) %{_libexecdir}/mod_env.so
%attr(755,root,root) %{_libexecdir}/mod_include.so
%attr(755,root,root) %{_libexecdir}/mod_log_agent.so
%attr(755,root,root) %{_libexecdir}/mod_log_config.so
%attr(755,root,root) %{_libexecdir}/mod_log_referer.so
%attr(755,root,root) %{_libexecdir}/mod_mime.so
%attr(755,root,root) %{_libexecdir}/mod_mime_magic.so
%attr(755,root,root) %{_libexecdir}/mod_negotiation.so
%attr(755,root,root) %{_libexecdir}/mod_setenvif.so
%attr(755,root,root) %{_libexecdir}/mod_speling.so
%attr(755,root,root) %{_libexecdir}/mod_userdir.so

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

%files mod_actions
%attr(755,root,root) %{_libexecdir}/mod_actions.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_actions.html

%files mod_auth_anon
%attr(755,root,root) %{_libexecdir}/mod_auth_anon.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_auth_anon.html

%files mod_define
%attr(755,root,root) %{_libexecdir}/mod_define.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_define.html

%files mod_digest
%attr(755,root,root) %{_libexecdir}/mod_digest.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_digest.html

%files mod_dir
%attr(755,root,root) %{_libexecdir}/mod_dir.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_dir.html

%files mod_expires
%attr(755,root,root) %{_libexecdir}/mod_expires.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_expires.html

%files mod_headers
%attr(755,root,root) %{_libexecdir}/mod_headers.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_headers.html

%files mod_mmap_static
%attr(755,root,root) %{_libexecdir}/mod_mmap_static.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_mmap_static.html

%files mod_imap
%attr(755,root,root) %{_libexecdir}/mod_imap.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_imap.html

%files mod_info
%attr(755,root,root) %{_libexecdir}/mod_info.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_info.html

%files mod_proxy
%attr(755,root,root) %{_libexecdir}/libproxy.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_proxy.html
%dir %attr(750,http,http) /var/cache/apache

%files mod_rewrite
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_rewrite.html

%files mod_status
%attr(755,root,root) %{_libexecdir}/mod_status.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_status.html

%files mod_usertrack
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_usertrack.html

%files mod_unique_id
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_unique_id.html

%files mod_vhost_alias
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
%attr(644,root,root) %{_datadir}/manual/mod/mod_vhost_alias.html
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/virtual-host.conf

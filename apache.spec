# TODO:
# - mod_case_filter
# - mod_case_filter_in
# - mod_optional_fn_{export,import}
# - mod_optional_hook_{export,import}
# - config examples for mod_*
# - switch from worker to perchild when it will be working in apache
%include	/usr/lib/rpm/macros.perl
Summary:	The most widely used Web server on the Internet
Summary(de):	Leading World Wide Web-Server
Summary(es):	Servidor HTTPD para proveer servicios WWW
Summary(fr):	Le serveur web le plus utilise sur Internet
Summary(pl):	Serwer WWW (World Wide Web)
Summary(pt_BR):	Servidor HTTPD para prover servi�os WWW
Summary(tr):	Lider WWW taray�c�
Name:		apache
Version:	2.0.35
Release:	0.5
License:	Apache Group License
Group:		Networking/Daemons
URL:		http://httpd.apache.org/
Source0:	http://www.apache.org/dist/httpd/httpd-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	%{name}-icons.tar.gz
Source4:	%{name}.sysconfig
Source6:	%{name}-httpd.conf
Source8:	%{name}-mod_vhost_alias.conf
Source9:	%{name}-mod_status.conf
Source10:	%{name}-mod_proxy.conf
Source11:	%{name}-mod_info.conf
Source12:	%{name}-mod_ssl.conf
Source13:	%{name}-mod_dav.conf
Patch0:		%{name}-apxs.patch
Patch1:		%{name}-configdir_skip_backups.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	automake
BuildRequires:	openssl-devel
BuildRequires:	openssl-tools
BuildRequires:	db4-devel
BuildRequires:	zlib-devel
BuildRequires:	expat-static
BuildRequires:	perl-devel >= 5.004
BuildRequires:	gdbm-devel
BuildRequires:	byacc
BuildRequires:	rpm-perlprov >= 4.0.4
Provides:	httpd = %{version}
Provides:	webserver = %{version}
Prereq:		/sbin/chkconfig
Prereq:		/usr/sbin/useradd
Prereq:		/usr/bin/getgid
Prereq:		/bin/id
Prereq:		sh-utils
Prereq:		rc-scripts
Prereq:		perl
Requires:	mailcap
Requires:	/etc/mime.types
Requires:	psmisc >= 20.1
Requires:	libtool
Obsoletes:	apache-extra
Obsoletes:	apache6
Obsoletes:	apache-doc
Obsoletes:	indexhtml

%define		_sysconfdir	/etc/httpd
%define		_includedir	%{_prefix}/include/apache
%define		_datadir	/home/services/httpd
%define		_libexecdir	%{_libdir}/apache

%description
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%description -l de
Apache ist ein voll funktionsf�higer Web-Server, der kostenlos
erh�ltlich und weit verbreitet ist.

%description -l es
El servidor web Apache es el mejor servidor gratuito disponible en el
mundo UNIX hoy. Usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vean documentos y sometan datos remotamente. Puede
ejecutar varias funciones diferentes, incluyendo funciones de proxy y
cach�, y nos ofrece caracter�sticas como monitor de estado, conversi�n
din�mica de tipo, y otras m�s.

%description -l fr
Apache est un serveur Web puissant, efficace, gratuit et complet.
Apache est aussi le serveur Web le plus populaire sur Internet.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj�c ten pakiet
b�dziesz m�g� prezentowa� w�asne strony WWW w sieci internet.

%description -l pt_BR
O servidor web Apache � o melhor servidor gratuito dispon�vel no mundo
UNIX hoje. Ele usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vejam documentos e submetam dados remotamente. Ele
pode executar v�rias fun��es diferentes, incluindo fun��es de proxy e
cache, e oferece caracter�sticas como monitor de status, convers�o
din�mica de tipo, e mais.

%description -l tr
Apache serbest da��t�lan ve �ok kullan�lan yetenekli bir web
sunucusudur.

%package suexec
Summary:	Apache suexec wrapper
Summary(pl):	Suexec wrapper do serwera www Apache
Group:		Development/Tools
Requires:	%{name} = %{version}

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and
SSI programs under user IDs different from the user ID of the calling
web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description suexec -l pl
SuEXEC umo�liwia serwerowi Apache uruchamianie program�w CGI i SSI z
innym UID ni� wywo�uj�cy je serwer. Normalnie programy CGI i SSI s�
wykonywane jako taki sam u�ytkownik jak serwer WWW.

%package devel
Summary:	Module development tools for the Apache web server
Summary(es):	Archivos de inclusi�n del Apache para desarrollo de m�dulos
Summary(fr):	Les outils de developpement de modules pour le serveur web Apache
Summary(pl):	Pliki nag��wkowe do tworzenai modu��w rozszerze� do serwera www Apache
Summary(pt_BR):	Arquivos de inclus�o do Apache para desenvolvimento de m�dulos
Group:		Networking/Utilities
Requires:	%{name} = %{version}
Requires:	apr-devel = %{version}

%description devel
The apache-devel package contains header files for Apache.

%description devel -l es
Este paquete contiene los archivos de inclusi�n para el Apache, bien
como el utilitario apxs para la construcci�n de objetos compartidos
din�micos (DSOs). Ha ce falta instalar este paquete si deseas compilar
o desarrollar m�dulos adicionales para Apache.

%description devel -l fr
Le package apache-devel contient le code source pour le serveur Web
Apache et le binaire APXS dont vous aurez besoin pour construire des
Objets Dynamiques Partages (DSOs) pour Apache.

%description devel -l pl
Pliki nag��wkowe dla serwera WWW Apache.

%description devel -l pt_BR
Este pacote contem os arquivos de inclus�o para o Apache, bem como o
utilit�rio apxs para a constru��o de objetos compartilhados din�micos
(DSOs). Este pacote precisa ser instalado se voc� deseja compilar ou
desenvolver m�dulos adicionais para o Apache.

%package static
Summary:	Static Apache web server libraries
Summary(pl):	Statyczne biblioteki serwera www Apache
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
The apache-static package contains static libraries for Apache.

%description static -l pl
Styatyczne biblioteki serwera Apache.

%package mod_actions
Summary:	Apache module for run CGI whenever a file of a certain type is requested
Summary(pl):	Modu� dla apache do uruchamiania skrypt�w cgi
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_actions
This package contains mod_actions module. This module lets you run CGI
scripts whenever a file of a certain type is requested. This makes it
much easier to execute scripts that process files.

%description mod_actions -l pl
Ten modu� pozwala na uruchamianie skrypt�w w momencie gdy nadchodzi
��danie pobrania pliku okre�lonego typu.

%package mod_auth
Summary:	Apache module with user authentication using textual files
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_auth
This package contains mod_auth module. It provides for user
authentication using textual files.

%description mod_auth -l pl
Ten pakiet zawiera modu� mod_auth. S�u�y on do autentykacji przy
u�yciu plik�w tekstowych.

%package mod_auth_anon
Summary:	Apache module with "anonymous" user access authentication
Summary(pl):	Modu� apache oferuj�cy anonimow� autoryzacj� u�ytkownia
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_auth_anon
This package contains mod_auth_anon module. It allows "anonymous" user
access to authenticated areas. It does access control in a manner
similar to anonymous-ftp sites; i.e. have a 'magic' user id
'anonymous' and the email address as a password. These email addresses
can be logged. Combined with other (database) access control methods,
this allows for effective user tracking and customization according to
a user profile while still keeping the site open for 'unregistered'
users. One advantage of using Auth-based user tracking is that, unlike
magic-cookies and funny URL pre/postfixes, it is completely browser
independent and it allows users to share URLs.

%description mod_auth_anon -l pl
Ten modu� oferuje anonimow� autoryzacj� u�ytkownia podobnie do
anonimowych serwer�w ftp (u�ytkownik ,,anonymous'' oraz has�o w
postaci adresu pocztowego u�ytkownika).

%package mod_auth_dbm
Summary:	Apache module with user authentication which uses DBM files
Summary(pl):	Modu� apache z mechanizmem autentykacji u�ywaj�cym plik�w DBM
Group:		Networking/Daemons
Obsoletes:	%{name}-mod_auth_db
Requires:	%{name} = %{version}

%description mod_auth_dbm
This module provides for HTTP Basic Authentication, where the
usernames and passwords are stored in DBM type database files. It is
an alternative to the plain text password files provided by mod_auth.

%description mod_auth_dbm -l pl
Ten modu� dostarcza Pros� Autoryzacj� HTTP gdzie u�ytkownicy oraz ich
has�a s� trzymane w plikach bazy typu DBM.

%package mod_auth_digest
Summary:	Apache user authentication module using MD5 Digest Authentication
Summary(pl):	Modu� apache do autoryzacji MD5
Group:		Networking/Daemons
Obsoletes:	apache-mod_digest
Requires:	%{name} = %{version}

%description mod_auth_digest
This package contains mod_digest module. It provides user
authentication using MD5 Digest Authentication.

%description mod_auth_digest -l pl
Modu� ten dostarcza metod� autoryzacji bazuj�c� na MD5 Digest
Authentication.

%package mod_cache
Summary:	Content cache keyed to URIs
Summary(pl):	Pami�� podr�czna wg klucza URI
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_cache
mod_cache implements an RFC 2616 compliant HTTP content cache that can
be used to cache either local or proxied content. Two storage
management modules are included in the base Apache distribution:
mod_disk_cache implements a disk based storage manager (generally used
for proxy caching) and mod_mem_cache implements an in-memory based
storage manager (primarily useful for caching local content).

%description mod_cache -l pl
Implementacja zgodnej z RFC 2616 pami�ci podr�cznej, kt�ra mo�e by�
u�ywana do zapami�tywania zawarto�ci lokalnej lub dost�pnej przez
proxy. Do��czono dwa modu�y pozwalaj�ce magazynowa� dane w pami�ci
(g��wnie u�yteczne przy cacheowaniu lokalnej zawarto�ci) oraz na dysku
(u�ywane do cacheowania proxy).

%package mod_cgid
Summary:	Execution of CGI scripts using an external CGI daemon
Summary(pl):	Uruchamianie zewn�trznych skrypt�w CGI za pomoc� daemona CGI
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_cgid
Execution of CGI scripts using an external CGI daemon.

%description mod_cgid -l pl
Uruchamianie zewn�trznych skrypt�w CGI za pomoc� daemona CGI

%package mod_charset_lite
Summary:	Specify character set translation or recoding
Summary(pl):	Translacja lub przekodowywanie znak�w
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_charset_lite
Specify character set translation or recoding.

%description mod_charset_lite -l pl
Translacja lub przekodowywanie znak�w.

%package mod_dav
Summary:	Apache module - Distributed Authoring and Versioning
Summary(pl):	Modu� apache - Rozdzielone Autorstwo i Wersjonowanie
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_dav
This module provides class 1 and class 2 WebDAV ('Web-based
Distributed Authoring and Versioning') functionality for Apache. This
extension to the HTTP protocol allows creating, moving, copying, and
deleting resources and collections on a remote web server.

%description mod_dav -l pl
Modu� dostarcza klas� 1 oraz klas� 2 WebDAV (Bazuj�cy na WWWW
Rozdzielone Autorstwo i Wersjonowanie). To rozszerzenie HTTP pozwala
na tworzenie, przesuwanie, kopiowanie oraz kasowanie zasob�w na
zdalnym serwerze www.

%package mod_deflate
Summary:	Apache module: Compress content before it is delivered to the client
Summary(pl):	Modu� kompresuj�cy dane przed przes�aniem ich do klienta
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_deflate
Compress content before it is delivered to the client.

%description mod_deflate -l pl
Modu� kompresuj�cy dane przed przes�aniem ich do klienta.

%package mod_dir
Summary:	Apache module for "trailing slash" redirects and serving directory index files
Summary(pl):	Modu� oferuj�cy przekierowania i serwowanie indeksu katalogu.
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_dir
This package contains mod_dir which provides "trailing slash"
redirects and serving directory index files.

%description mod_dir -l pl
Modu� oferuj�cy przekierowania i serwowanie indeksu katalogu.

%package mod_headers
Summary:	Apache module allows for the customization of HTTP response headers
Summary(pl):	Modu� pozwalaj�cy na modyfikacj� nag��wk�w HTTP
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_headers
This package contains mod_headers module. The module allows for the
customization of HTTP response headers. Headers can be merged,
replaced or removed.

%description mod_headers -l pl
Modu� pozwalaj�cy na ��czenie, usuwania, zamian� nag��wk�w HTTP
wysy�anych do przegl�darki.

%package mod_imap
Summary:	Apache module with imap-file handler
Summary(pl):	Modu� z obs�ug� imap-file
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_imap
This package contains mod_imap module. It provides for .map files,
replacing the functionality of the imagemap CGI program. Any directory
or document type configured to use the handler imap-file.

%description mod_imap -l pl
Modu� umozliwiaj�cy obs�ug� plik�w .map (imap-file handler)

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Summary(pl):	Modu� dostarczaj�cy informacji na temat serwera.
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_info
This package contains mod_info module. It provides a comprehensive
overview of the server configuration including all installed modules
and directives in the configuration files.

%description mod_info -l pl
Modu� dostarczaj�cy informacji o konfiguracji serwera, zainstalowanych
modu�ach itp.

%package mod_proxy
Summary:	Apache module with Web proxy
Summary(pl):	Modu� dodaj�cy obs�ug� serwera proxy
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_proxy

This package contains module with implementation a proxy/cache for
Apache. It implements proxying capability for FTP, CONNECT (for SSL),
HTTP/0.9, HTTP/1.0 and HTTP/1.1. The module can be configured to
connect to other proxy modules for these and other protocols.

%description mod_proxy -l pl
Modu� zawiera implementacj� serwera proxy/cache dla Apache.
Iplementacja zawiera obs�ug� FTP, CONNECT (dla SSL), HTTP/0.9,
HTTP/1.0 i HTTP/1.1.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Summary(pl):	Modu� do ,,przepisywania'' adres�w URL w locie
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to
rewrite requested URLs on the fly.

%description mod_rewrite -l pl
Modu� oferuj�cy mo�liwo�� ,,przepisywania'' adres�w URL w locie.

%package mod_ssl
Summary:	Apache module: Strong cryptography using the Secure Sockets Layer (SSL)
Summary(pl):	Modu� apache: Silna kryptografia z u�yciem SSL
Group:		Networking/Daemons
Epoch:		1
Requires:	%{name} = %{version}

%description mod_ssl
Strong cryptography using the Secure Sockets Layer (SSL).

%description mod_ssl -l pl
Silna kryptografia z u�yciem SSL.

%package mod_status
Summary:	Server status report module for apache
Summary(pl):	Modu� dostarczaj�cy informacje statystyczne o serwerze.
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_status
The Status module allows a server administrator to find out how well
their server is performing. A HTML page is presented that gives the
current server statistics in an easily readable form. If required this
page can be made to automatically refresh (given a compatible
browser).

%description mod_status -l pl
Modu� pozwala administratorowi na przegl�danie statystyk dotycz�cych
pracy serwera apache (w postaci strony HTML).

%package mod_usertrack
Summary:	Apache module for user tracking using cookies
Summary(pl):	Modu� s�u��cy do �ledzenia ,,ciasteczek''.
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_usertrack
This package contains the user tracking module which did its own
logging using CookieLog directory. This module allow multiple log
files.

%description mod_usertrack -l pl
Modu� pozwalaj�cy na �ledzenie ,,ciasteczek''.

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Summary(pl):	Modu� dodaj�cy obs�ug� host�w wirtualnych.
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

%description mod_vhost_alias -l pl
Modu� umo�liwia na dynamiczne konfigurowanie masowej ilo�ci serwer�w
wirtualnych.

%package mod_unique_id
Summary:	Apache module which provides a magic token for each request
Summary(pl):	Modu� nadaj�cy ka�demu ��daniu unikalny token
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_unique_id
This package contains the mod_unique_id. This module provides a magic
token for each request which is guaranteed to be unique across "all"
requests under very specific conditions. The unique identifier is even
unique across multiple machines in a properly configured cluster of
machines. The environment variable UNIQUE_ID is set to the identifier
for each request. Unique identifiers are useful for various reasons
which are beyond the scope of this document.

%description mod_unique_id -l pl
Modu� nadaje przy ka�dym ��daniu token unikalny w ramach wszystkich
��da�, nawet w ramach poprawnie skonfigurowanego klastra z wielu
maszyn. Modu� ustawia przy ka�dym ��daniu zmienn� �rodowiskow�
UNIQUE_ID.

%package mod_expires
Summary:	Apache module which generates Expires HTTP headers
Summary(pl):	Modu� generuj�cy nag��wki HTTP Expires
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_expires
This module controls the setting of the Expires HTTP header in server
responses. The expiration date can set to be relative to either the
time the source file was last modified, or to the time of the client
access.

%description mod_expires -l pl
Modu� kontroluje ustawianie nag��wka HTTP Expires. Data wyga�ni�cia
wa�no�ci mo�e by� ustalana w zale�no�ci od czasu modyfikacji plik�w
�r�d�owych lub odwo�ania klienta.

%package mod_file_cache
Summary:	Apache module: Caches a static list of files in memory
Summary(pl):	Modu� cacheuj�cy statyczn� list� plik�w w pami�ci
Group:		Networking/Daemons
Obsoletes:	%{name}-mmap_static
Requires:	%{name} = %{version}

%description mod_file_cache
Caches a static list of files in memory.

%description mod_file_cache -l pl
Modu� cacheuj�cy statyczn� list� plik�w w pami�ci.

%package -n apr
Summary:	The Apache Portable Runtime library
Summary(pl):	Przeno�na biblioteka Apache
Group:		Libraries

%description -n apr
The Apache Portable Run-time libraries have been designed to provide a
common interface to low level routines across any platform.

%description -n apr -l pl
Przeno�na biblioteka Apache zosta�a zaprojektowana w celu dostarczania
popularnego i jednolitego interfejsu do niskopoziomowych funkcji na
dowolnej platformie.

%package -n apr-devel
Summary:	The includes and linker libraries for development with APR
Summary(pl):	Pliki nag��wkowe, biblioteki dla linkera APR
Group:		Development/Libraries
Requires:	apr = %{version}

%description -n apr-devel
The includes and linker libraries for development with APR.

%description -n apr-devel -l pl
Pliki nag��wkowe, biblioteki dla linkera APR.

%package -n apr-static
Summary:	Static APR libraries.
Summary(pl):	Statyczne biblioteki APR.
Group:		Development/Libraries
Requires:	apr-devel = %{version}

%description -n apr-static
Static APR libraries.

%description -n apr-static -l pl
Statyczne biblioteki APR.

%prep
%setup -q -n httpd-%{version}
%patch0 -p1
%patch1 -p1

%build
cp -f %{_prefix}/share/automake/config.* srclib/pcre/
cp -f %{_prefix}/share/automake/config.* srclib/apr/build/
cp -f %{_prefix}/share/automake/config.* srclib/apr-util/xml/expat/conftools/
%configure2_13 \
	--enable-layout=PLD \
	--enable-modules=all \
	--enable-mods-shared=all \
	--enable-auth-anon	 \
	--enable-auth-dbm \
	--enable-auth-digest \
	--enable-file-cache \
	--enable-echo \
	--enable-cache \
	--enable-charset-lite \
	--enable-mem-cache \
	--enable-disk-cache \
	--enable-ext-filter \
	--enable-case-filter \
	--enable-case-filter-in \
	--enable-deflate \
	--with-z=%{_prefix} \
	--enable-mime-magic \
	--enable-cern-meta \
	--enable-expires \
	--enable-headers \
	--enable-usertrack \
	--enable-unique-id \
	--enable-proxy \
	--enable-proxy-connect \
	--enable-proxy-ftp \
	--enable-proxy-http \
	--enable-ssl \
	--enable-optional-hook-export \
	--enable-optional-hook-import \
	--enable-optional-fn-import \
	--enable-optional-fn-export \
	--enable-dav \
	--enable-info \
	--enable-suexec \
	--enable-cgi \
	--enable-cgid \
	--enable-dav-fs \
	--enable-vhost-alias \
	--enable-speling \
	--enable-rewrite \
	--enable-so \
	--with-mpm=worker \
	--with-suexec-bin=%{_sbindir} \
	--with-suexec-caller=http \
	--with-suexec-docroot=%{_datadir} \
	--with-suexec-uidmin=500 \
	--with-suexec-gidmin=500 \
	--with-suexec-umask=077

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT%{_var}/log/{httpd,archiv/httpd}
install -d $RPM_BUILD_ROOT%{_var}/{run,cache}/apache

%{makeinstall} \
	prefix=%{_sysconfdir}/httpd \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	installbuilddir=$RPM_BUILD_ROOT%{_sysconfdir}/build \
	libexecdir=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	iconsdir=$RPM_BUILD_ROOT%{_datadir}/icons \
	errordir=$RPM_BUILD_ROOT%{_datadir}/error \
	htdocsdir=$RPM_BUILD_ROOT%{_datadir}/html \
	manualdir=$RPM_BUILD_ROOT%{_datadir}/manual \
	cgidir=$RPM_BUILD_ROOT%{_datadir}/cgi-bin \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	localstatedir=$RPM_BUILD_ROOT%{_localstatedir} \
	runtimedir=$RPM_BUILD_ROOT{_var}/run \
	logdir=$RPM_BUILD_ROOT%{_var}/log/httpd \
	proxycachedir=$RPM_BUILD_ROOT%{_var}/cache/httpd

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -d $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/build \
	$RPM_BUILD_ROOT%{_libexecdir}/build

perl -pi -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{_libexecdir}/build/config_vars.mk
perl -pi -e "s#-pthread#-lpthread#g" $RPM_BUILD_ROOT%{_libdir}/lib*.la

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/apache

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,agent,referer}_log

CFG="$RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf/"

install %{SOURCE6}  $CFG/10_httpd.conf
install %{SOURCE8}  $CFG/20_mod_vhost_alias.conf
install %{SOURCE9}  $CFG/25_mod_status.conf
install %{SOURCE10} $CFG/30_mod_proxy.conf
install %{SOURCE11} $CFG/35_mod_info.conf
install %{SOURCE12} $CFG/40_mod_ssl.conf
install %{SOURCE13} $CFG/45_mod_dav.conf

echo "LoadModule actions_module       %{_libexecdir}/mod_actions.so" > $CFG/50_mod_actions.conf
echo "LoadModule auth_module          %{_libexecdir}/mod_auth.so" > $CFG/51_mod_auth.conf
echo "LoadModule auth_anon_module     %{_libexecdir}/mod_auth_anon.so" > $CFG/52_mod_auth_anon.conf
echo "LoadModule auth_dbm_module      %{_libexecdir}/mod_auth_dbm.so" > $CFG/53_mod_auth_dbm.conf
echo "LoadModule auth_digest_module   %{_libexecdir}/mod_auth_digest.so" > $CFG/54_mod_auth_digest.conf
echo "LoadModule cache_module         %{_libexecdir}/mod_cache.so
LoadModule mem_cache_module     %{_libexecdir}/mod_mem_cache.so
LoadModule disk_cache_module    %{_libexecdir}/mod_disk_cache.so" > $CFG/55_mod_cache.conf
echo "LoadModule cgid_module          %{_libexecdir}/mod_cgid.so" > $CFG/56_mod_cgid.conf
echo "LoadModule charset_lite_module  %{_libexecdir}/mod_charset_lite.so" > $CFG/57_mod_charset_lite.conf
echo "LoadModule deflate_module       %{_libexecdir}/mod_deflate.so" > $CFG/58_mod_deflate.conf
echo "LoadModule dir_module           %{_libexecdir}/mod_dir.so" > $CFG/59_mod_dir.conf
echo "LoadModule expires_module       %{_libexecdir}/mod_expires.so" > $CFG/60_mod_expires.conf
echo "LoadModule file_cache_module    %{_libexecdir}/mod_file_cache.so" > $CFG/61_mod_file_cache.conf
echo "LoadModule headers_module       %{_libexecdir}/mod_headers.so" > $CFG/62_mod_headers.conf
echo "LoadModule imap_module          %{_libexecdir}/mod_imap.so" > $CFG/63_mod_imap.conf
echo "LoadModule rewrite_module       %{_libexecdir}/mod_rewrite.so" > $CFG/64_mod_rewrite.conf
echo "LoadModule usertrack_module     %{_libexecdir}/mod_usertrack.so" > $CFG/65_mod_usertrack.conf
echo "LoadModule unique_id_module     %{_libexecdir}/mod_unique_id.so" > $CFG/66_mod_unique_id.conf

ln -sf index.html.en $RPM_BUILD_ROOT%{_datadir}/html/index.html

gzip -9nf ABOUT_APACHE CHANGES README ROADMAP

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid http`" ]; then
	if [ "`getgid http`" != "51" ]; then
		echo "Warning: group http haven't gid=51. Correct this before installing apache" 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 51 -r -f http
fi
if [ -n "`id -u http 2>/dev/null`" ]; then
	if [ "`id -u http`" != "51" ]; then
		echo "Warning: user http haven't uid=51. Correct this before installing apache" 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 51 -r -d /home/httpd -s /bin/false -c "HTTP User" -g http http 1>&2
fi

%post
/sbin/ldconfig
/sbin/chkconfig --add httpd
umask 137
touch /var/log/httpd/{access,error,agent,referer}_log
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd stop 1>&2
	fi
	/sbin/chkconfig --del httpd
fi

%postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	/usr/sbin/userdel http
	/usr/sbin/groupdel http
fi

%post mod_actions
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_actions
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_auth
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_auth
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_auth_anon
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_auth_anon
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_auth_dbm
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_auth_dbm
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_cache
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_cache
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_cgid
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_cgid
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_charset_lite
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_charset_lite
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_dav
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_dav
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_auth_digest
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_auth_digest
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_deflate
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_deflate
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_dir
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_dir
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_expires
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_expires
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_file_cache
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_file_cache
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_headers
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_headers
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_imap
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_imap
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_info
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_info
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_proxy
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_proxy
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_rewrite
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_rewrite
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_ssl
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_ssl
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_status
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_status
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_usertrack
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_usertrack
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_unique_id
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_unique_id
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_vhost_alias
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_vhost_alias
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post -n apr -p /sbin/ldconfig
%postun -n apr -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%doc docs/conf/mime.types

%attr(754,root,root) /etc/rc.d/init.d/httpd

%attr(750,root,root) %dir %{_sysconfdir}
%attr(750,root,root) %dir %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_httpd.conf
%attr(640,root,root) %{_sysconfdir}/magic
%attr(755,root,root) %dir %{_libexecdir}/build
%attr(755,root,root) %{_libexecdir}/build/*.mk
%attr(755,root,root) %{_libexecdir}/build/*.sh

%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/*
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/*

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/mod_access.so
%attr(755,root,root) %{_libexecdir}/mod_alias.so
%attr(755,root,root) %{_libexecdir}/mod_asis.so
%attr(755,root,root) %{_libexecdir}/mod_autoindex.so
%attr(755,root,root) %{_libexecdir}/mod_cern_meta.so
%attr(755,root,root) %{_libexecdir}/mod_cgi.so
%attr(755,root,root) %{_libexecdir}/mod_env.so
%attr(755,root,root) %{_libexecdir}/mod_include.so
%attr(755,root,root) %{_libexecdir}/mod_log_config.so
%attr(755,root,root) %{_libexecdir}/mod_mime.so
%attr(755,root,root) %{_libexecdir}/mod_mime_magic.so
%attr(755,root,root) %{_libexecdir}/mod_negotiation.so
%attr(755,root,root) %{_libexecdir}/mod_setenvif.so
%attr(755,root,root) %{_libexecdir}/mod_speling.so
%attr(755,root,root) %{_libexecdir}/mod_userdir.so

%attr(755,root,root) %{_sbindir}/htdigest

%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/checkgid
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs

%attr(755,root,root) %{_libdir}/lib*.so.*

%dir %attr(770,root,http) /var/run/apache

%{_mandir}/man1/htdigest.1*
%{_mandir}/man8/*

%attr(750,root,root) %dir /var/log/httpd
%attr(750,root,root) %dir /var/log/archiv/httpd
%attr(640,root,root) %ghost /var/log/httpd/*

%dir %{_datadir}
%dir %{_datadir}/manual
%{_datadir}/manual/*.html
%{_datadir}/manual/*.html.en
%lang(ja) %{_datadir}/manual/*.html.ja.jis
%lang(de) %{_datadir}/manual/*.html.de
%lang(fr) %{_datadir}/manual/*.html.fr
%{_datadir}/manual/developer
%{_datadir}/manual/faq
%dir %{_datadir}/manual/howto
%doc %{_datadir}/manual/howto/*.en
%{_datadir}/manual/howto/*.html
%lang(ja) %{_datadir}/manual/howto/*.ja.jis
%dir %{_datadir}/manual/images
%{_datadir}/manual/images/[achips]*
%{_datadir}/manual/misc
%dir %{_datadir}/manual/mod
%{_datadir}/manual/mod/[cdfhipw]*.html
%{_datadir}/manual/mod/mpm*.html
%{_datadir}/manual/mod/mod_access.html
%{_datadir}/manual/mod/mod_alias.html
%{_datadir}/manual/mod/mod_asis.html
%{_datadir}/manual/mod/mod_autoindex.html
%{_datadir}/manual/mod/mod_cern_meta.html
%{_datadir}/manual/mod/mod_cgi.html
%{_datadir}/manual/mod/mod_env.html
%{_datadir}/manual/mod/mod_include.html
%{_datadir}/manual/mod/mod_log_config.html
%{_datadir}/manual/mod/mod_mime*.html
%{_datadir}/manual/mod/mod_negotiation.html
%{_datadir}/manual/mod/mod_setenvif.html
%{_datadir}/manual/mod/mod_speling.html
%{_datadir}/manual/mod/mod_userdir.html
%{_datadir}/manual/platform
%{_datadir}/manual/programs
%dir %{_datadir}/manual/search
%doc%attr(755,root,root) %{_datadir}/manual/search/manual-index.cgi
%{_datadir}/manual/style

# Having all index.html.LANG files here is very bad idea.
%attr(755,root,root) %dir %{_datadir}/html
%config(noreplace,missingok) %{_datadir}/html/index.html
%config(noreplace,missingok) %{_datadir}/html/index.html.en
%{_datadir}/html/*.gif
%dir %{_datadir}/icons
%{_datadir}/icons/*.gif
%dir %{_datadir}/icons/small
%{_datadir}/icons/small/*.gif
%attr(755,root,root) %{_datadir}/cgi-bin

%{_datadir}/error

%files suexec
%defattr(644,root,root,755)
%attr(4755,root,root) %{_sbindir}/suexec
%attr(755,root,root) %{_libexecdir}/mod_suexec.so
%{_datadir}/manual/mod/mod_suexec.html

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apu-config
%{_includedir}
%exclude %{_includedir}/apr*.h
%{_libdir}/aprutil.exp
%{_libexecdir}/*.exp
%attr(755,root,root) %{_libdir}/libaprutil.so
%attr(755,root,root) %{_libdir}/libaprutil.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files mod_actions
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_actions.conf
%attr(755,root,root) %{_libexecdir}/mod_actions.so
%{_datadir}/manual/mod/mod_actions.html

%files mod_auth
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_auth.so
%attr(755,root,root) %{_sbindir}/htpasswd
%{_datadir}/manual/mod/mod_auth.html
%{_mandir}/man1/htpasswd.1*

%files mod_auth_anon
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_auth_anon.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_anon.so
%{_datadir}/manual/mod/mod_auth_anon.html

%files mod_auth_dbm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_auth_dbm.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_dbm.so
%attr(755,root,root) %{_sbindir}/dbmmanage
%attr(755,root,root) %{_sbindir}/htdbm
%{_datadir}/manual/mod/mod_auth_dbm.html
%{_mandir}/man1/dbmmanage.1*

%files mod_auth_digest
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_auth_digest.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_digest.so
%{_datadir}/manual/mod/mod_auth_digest.html

%files mod_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_cache.conf
%attr(755,root,root) %{_libexecdir}/mod_cache.so
%attr(755,root,root) %{_libexecdir}/mod_disk_cache.so
%attr(755,root,root) %{_libexecdir}/mod_mem_cache.so
%{_datadir}/manual/mod/mod_cache.html

%files mod_cgid
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_cgid.conf
%attr(755,root,root) %{_libexecdir}/mod_cgid.so
%{_datadir}/manual/mod/mod_cgid.html

%files mod_charset_lite
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_charset_lite.conf
%attr(755,root,root) %{_libexecdir}/mod_charset_lite.so
%{_datadir}/manual/mod/mod_charset_lite.html

%files mod_dav
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_dav.conf
%attr(755,root,root) %{_libexecdir}/mod_dav*.so
%{_datadir}/manual/mod/mod_dav*.html

%files mod_deflate
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_deflate.conf
%attr(755,root,root) %{_libexecdir}/mod_deflate.so
%{_datadir}/manual/mod/mod_deflate.html

%files mod_dir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_dir.conf
%attr(755,root,root) %{_libexecdir}/mod_dir.so
%{_datadir}/manual/mod/mod_dir.html

%files mod_expires
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_expires.conf
%attr(755,root,root) %{_libexecdir}/mod_expires.so
%{_datadir}/manual/mod/mod_expires.html

%files mod_file_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_file_cache.conf
%attr(755,root,root) %{_libexecdir}/mod_file_cache.so
%{_datadir}/manual/mod/mod_file_cache.html

%files mod_headers
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_headers.conf
%attr(755,root,root) %{_libexecdir}/mod_headers.so
%{_datadir}/manual/mod/mod_headers.html

%files mod_imap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_imap.conf
%attr(755,root,root) %{_libexecdir}/mod_imap.so
%{_datadir}/manual/mod/mod_imap.html

%files mod_info
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_info.conf
%attr(755,root,root) %{_libexecdir}/mod_info.so
%{_datadir}/manual/mod/mod_info.html

%files mod_proxy
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_proxy.conf
%attr(755,root,root) %{_libexecdir}/mod_proxy*.so
%doc %{_datadir}/manual/mod/mod_proxy*.html
%attr(770,root,http) /var/cache/apache

%files mod_rewrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so
%{_datadir}/manual/mod/mod_rewrite.html
%{_datadir}/manual/images/mod_rewrite*

%files mod_ssl
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_ssl.conf
%attr(755,root,root) %{_libexecdir}/mod_ssl.so
%{_datadir}/manual/ssl
%{_datadir}/manual/mod/mod_ssl.html

%files mod_status
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_status.conf
%attr(755,root,root) %{_libexecdir}/mod_status.so
%{_datadir}/manual/mod/mod_status.html

%files mod_usertrack
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_usertrack.conf
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so
%{_datadir}/manual/mod/mod_usertrack.html

%files mod_unique_id
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_unique_id.conf
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so
%{_datadir}/manual/mod/mod_unique_id.html

%files mod_vhost_alias
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
%{_datadir}/manual/mod/mod_vhost_alias.html
%{_datadir}/manual/vhosts
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_vhost_alias.conf

%files -n apr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapr.so.*

%files -n apr-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apr-config
%{_includedir}/apr*.h
%{_libdir}/APRVARS
%{_libdir}/apr.exp
%attr(755,root,root) %{_libdir}/libapr.so
%attr(755,root,root) %{_libdir}/libapr.la

%files -n apr-static
%defattr(644,root,root,755)
%{_libdir}/libapr.a

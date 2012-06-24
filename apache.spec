# _without_ssl	- don't build with SSL support
# TODO:
# - mod_case_filter
# - mod_case_filter_in
# - mod_optional_fn_{export,import}
# - mod_optional_hook_{export,import}
# - mod_ext_filter
# - mod_echo
# - config examples for mod_*
# - switch from worker to perchild when it will be working in apache
# - check if all modules are (de)registered in %%post/%%postun
# - find smart way to deregister module if its moved from main package to subpackage (maybe test -f ?)
# - add %%post/%%postun to suexec
# - --with-suexec-gidmin=500 or =100 ?
# - --with-suexec-uidmin=500 or =1000 ?
%include	/usr/lib/rpm/macros.perl
# this is internal macro, don't change to %%apache_modules_api
%define		_apache_modules_api 20020903
Summary:	The most widely used Web server on the Internet
Summary(de):	Leading World Wide Web-Server
Summary(es):	Servidor HTTPD para proveer servicios WWW
Summary(fr):	Le serveur web le plus utilise sur Internet
Summary(pl):	Serwer WWW (World Wide Web)
Summary(pt_BR):	Servidor HTTPD para prover servi�os WWW
Summary(ru):	����� ���������� ���-������
Summary(tr):	Lider WWW taray�c�
Name:		apache
Version:	2.0.48
Release:	0.1
License:	Apache Group License
Group:		Networking/Daemons
Source0:	http://www.apache.org/dist/httpd/httpd-%{version}.tar.gz
# Source0-md5:	466c63bb71b710d20a5c353df8c1a19c
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	%{name}-icons.tar.gz
# Source3-md5:	2b085cbc19fd28536dc883f0b864cd83
Source4:	%{name}.sysconfig
Source6:	%{name}-httpd.conf
Source8:	%{name}-mod_vhost_alias.conf
Source9:	%{name}-mod_status.conf
Source10:	%{name}-mod_proxy.conf
Source11:	%{name}-mod_info.conf
Source12:	%{name}-mod_ssl.conf
Source13:	%{name}-mod_dav.conf
Source14:	%{name}-mod_dir.conf
Source20:	%{name}-server.crt
Source21:	%{name}-server.key
Patch0:		%{name}-configdir_skip_backups.patch
Patch1:		%{name}-layout.patch
Patch2:		%{name}-suexec.patch
Patch3:		%{name}-nolibs.patch
Patch4:		%{name}-apr.patch
URL:		http://httpd.apache.org/
BuildRequires:	db-devel
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel >= 1.8.3
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.7c}
%{!?_without_ssl:BuildRequires:	openssl-tools >= 0.9.7c}
BuildRequires:	perl-devel >= 5.004
BuildRequires:	rpm-perlprov >= 4.0.4
BuildRequires:	zlib-devel
BuildRequires:	libtool >= 1.5
BuildRequires:	apr-devel >= 1:0.9.4-1
BuildRequires:	apr-util-devel >= 1:0.9.4-1
PreReq:		perl-base
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires(post,preun):	/sbin/chkconfig
Requires(post,postun):	/sbin/ldconfig
Requires(post):	fileutils
Requires:	/etc/mime.types
Requires:	mailcap
Requires:	psmisc >= 20.1
Provides:	httpd = %{version}
Provides:	webserver = %{version}
Provides:	apache(modules-api) = %{_apache_modules_api}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	apache-extra
Obsoletes:	apache-doc
Obsoletes:	apache6
Obsoletes:	apache1
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

%description -l ru
Apache - ������, ��������������, ���������������������� � ��������
���������������� ���-������.

%description -l tr
Apache serbest da��t�lan ve �ok kullan�lan yetenekli bir web
sunucusudur.

%package suexec
Summary:	Apache suexec wrapper
Summary(pl):	Wrapper suexec do serwera WWW Apache
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

%package index
Summary:        Apache index.html* files
Summary(pl):    Pliki Apache index.html*
Group:          Documentation
Requires:       %{name} = %{version}

%description index
Apache index.html* files.

%description index -l pl
Pliki Apache index.html*.

%package devel
Summary:	Module development tools for the Apache web server
Summary(es):	Archivos de inclusi�n del Apache para desarrollo de m�dulos
Summary(fr):	Les outils de developpement de modules pour le serveur web Apache
Summary(pl):	Pliki nag��wkowe do tworzenia modu��w rozszerze� do serwera WWW Apache
Summary(pt_BR):	Arquivos de inclus�o do Apache para desenvolvimento de m�dulos
Summary(ru):	�������� ���������� ������� ��� ���-������� Apache
Group:		Networking/Utilities
Requires:	%{name} = %{version}
Requires:	apr-util-devel >= 1:0.9.4
Requires:	libtool
Obsoletes:	%{name}-static

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
Pliki nag��wkowe i inne zasoby niezb�dne przy budowaniu modu��w DSO
(Dynamic Shared Objects) dla Apache.

%description devel -l ru
�������� ���������� ������� ��� ���-������� Apache.

%description devel -l pt_BR
Este pacote contem os arquivos de inclus�o para o Apache, bem como o
utilit�rio apxs para a constru��o de objetos compartilhados din�micos
(DSOs). Este pacote precisa ser instalado se voc� deseja compilar ou
desenvolver m�dulos adicionais para o Apache.

%package mod_actions
Summary:	Apache module for run CGI whenever a file of a certain type is requested
Summary(pl):	Modu� Apache'a do uruchamiania skrypt�w CGI
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
Summary(pl):	Modu� Apache'a identyfikuj�cy u�ytkownik�w na podstawie plik�w tekstowych
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_auth
This package contains mod_auth module. It provides for user
authentication using textual files.

%description mod_auth -l pl
Ten pakiet zawiera modu� mod_auth. S�u�y on do sprawdzania to�samo�ci
u�ytkownik�w na podstawie plik�w tekstowych.

%package mod_auth_anon
Summary:	Apache module with "anonymous" user access authentication
Summary(pl):	Modu� Apache'a oferuj�cy autoryzacj� u�ytkownika "anonimowego"
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
Ten modu� oferuje autoryzacj� u�ytkownika "anonimowego" podobnie do
anonimowych serwer�w FTP (u�ytkownik "anonymous" oraz has�o w postaci
adresu pocztowego u�ytkownika).

%package mod_auth_dbm
Summary:	Apache module with user authentication which uses DBM files
Summary(pl):	Modu� Apache'a z mechanizmem identyfikacji korzystaj�cym z plik�w DBM
Group:		Networking/Daemons
Obsoletes:	%{name}-mod_auth_db
Requires:	%{name} = %{version}

%description mod_auth_dbm
This module provides for HTTP Basic Authentication, where the
usernames and passwords are stored in DBM type database files. It is
an alternative to the plain text password files provided by mod_auth.

%description mod_auth_dbm -l pl
Ten modu� udost�pnia Prost� Autoryzacj� HTTP, gdzie u�ytkownicy oraz
ich has�a s� trzymane w plikach bazy typu DBM.

%package mod_auth_digest
Summary:	Apache user authentication module using MD5 Digest Authentication
Summary(pl):	Modu� Apache'a do autoryzacji MD5
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
Uruchamianie zewn�trznych skrypt�w CGI za pomoc� demona CGI.

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
Summary(pl):	Modu� Apache'a - Rozproszone autorstwo i wersjonowanie
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_dav
This module provides class 1 and class 2 WebDAV ('Web-based
Distributed Authoring and Versioning') functionality for Apache. This
extension to the HTTP protocol allows creating, moving, copying, and
deleting resources and collections on a remote web server.

%description mod_dav -l pl
Modu� udost�pnia klas� 1 oraz klas� 2 WebDAV (Bazuj�cego na WWW
rozproszonego autorstwa i wersjonowania). To rozszerzenie HTTP pozwala
na tworzenie, przesuwanie, kopiowanie oraz kasowanie zasob�w na
zdalnym serwerze WWW.

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
Summary(pl):	Modu� oferuj�cy przekierowania i udost�pnianie informacji o zawarto�ci katalogu
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_dir
This package contains mod_dir which provides "trailing slash"
redirects and serving directory index files.

%description mod_dir -l pl
Modu� oferuj�cy przekierowania i udost�pnianie informacji o zawarto�ci
katalogu.

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
Modu� umo�liwiaj�cy obs�ug� plik�w .map (imap-file handler).

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Summary(pl):	Modu� udost�pniaj�cy informacje o serwerze
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_info
This package contains mod_info module. It provides a comprehensive
overview of the server configuration including all installed modules
and directives in the configuration files.

%description mod_info -l pl
Modu� udost�pniaj�cy informacje o konfiguracji serwera,
zainstalowanych modu�ach itp.

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
Implementacja zawiera obs�ug� FTP, CONNECT (dla SSL), HTTP/0.9,
HTTP/1.0 i HTTP/1.1.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Summary(pl):	Modu� do "przepisywania" adres�w URL w locie
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to
rewrite requested URLs on the fly.

%description mod_rewrite -l pl
Modu� oferuj�cy mo�liwo�� "przepisywania" adres�w URL w locie.

%package mod_ssl
Summary:	SSL/TLS module for the Apache HTTP server
Summary(pl):	Modu� SSL/TSL dla serwera Apache
Summary(ru):	������ SSL/TLS ��� ���-������� Apache
Group:		Networking/Daemons
Epoch:		1
Requires:	%{name} = %{version}

%description mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer Security
(TLS) protocols.

%description mod_ssl -l pl
Modu� mod_ssl udost�pnia wsparcie do silnej kryptografii dla serwera
Apache poprzez protoko�y SSL/TSL (Secure Sockets Layer/Transport Layer
Security).

%description mod_ssl -l ru
������ mod_ssl ������������ ��������� � ���-������� Apache ���������
���������� ���������� Secure Sockets Layer (SSL) � Transport Layer

%package mod_status
Summary:	Server status report module for apache
Summary(pl):	Modu� udost�pniaj�cy informacje statystyczne z serwera
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
Summary(pl):	Modu� s�u��cy do �ledzenia "ciasteczek"
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description mod_usertrack
This package contains the user tracking module which did its own
logging using CookieLog directory. This module allow multiple log
files.

%description mod_usertrack -l pl
Modu� pozwalaj�cy na �ledzenie "ciasteczek".

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Summary(pl):	Modu� dodaj�cy obs�ug� host�w wirtualnych
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
Summary(pl):	Modu� nadaj�cy ka�demu zapytaniu unikalny token
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
Modu� nadaje ka�demu zapytaniu token unikalny w ramach wszystkich
zapyta�, nawet w ramach poprawnie skonfigurowanego klastra z wielu
maszyn. Modu� ustawia przy ka�dym zapytaniu zmienn� �rodowiskow�
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
Summary(pl):	Modu� cache'uj�cy statyczn� list� plik�w w pami�ci
Group:		Networking/Daemons
Obsoletes:	%{name}-mmap_static
Requires:	%{name} = %{version}

%description mod_file_cache
Caches a static list of files in memory.

%description mod_file_cache -l pl
Modu� cache'uj�cy statyczn� list� plik�w w pami�ci.

%prep
%setup -q -n httpd-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# sanity check
MODULES_API=`awk '/#define MODULE_MAGIC_NUMBER_MAJOR/ {print $3}' include/ap_mmn.h`
if [ "$MODULES_API" != "%_apache_modules_api" ]; then
	echo "Set %%_apache_modules_api to $MODILES_API and rerun."
	exit 1
fi
./buildconf
%configure \
	--prefix=%{_libexecdir} \
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
	%{!?_without_ssl:--enable-ssl} \
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
	--with-suexec-bin=%{_sbindir}/suexec \
	--with-suexec-caller=http \
	--with-suexec-docroot=%{_datadir} \
	--with-suexec-logfile=/var/log/httpd/suexec_log \
	--with-suexec-uidmin=500 \
	--with-suexec-gidmin=500 \
	--with-suexec-umask=077 \
	--with-apr=%{_bindir} \
	--with-apr-util=%{_bindir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT%{_var}/{log/{httpd,archiv/httpd},{run,cache}/apache}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	installbuilddir=%{_sysconfdir}/build \
	prefix=%{_sysconfdir}/httpd \
	libexecdir=%{_libdir}/%{name} \
	iconsdir=%{_datadir}/icons \
	errordir=%{_datadir}/error \
	htdocsdir=%{_datadir}/html \
	manualdir=%{_datadir}/manual \
	cgidir=%{_datadir}/cgi-bin \
	runtimedir=%{_var}/run \
	logdir=%{_var}/log/httpd \
	proxycachedir=%{_var}/cache/httpd

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -d $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/build \
	$RPM_BUILD_ROOT%{_libexecdir}/build

perl -pi -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{_libexecdir}/build/*
perl -pi -e "s#$RPM_BUILD_DIR#%{_usrsrc}#g" $RPM_BUILD_ROOT%{_libexecdir}/build/*
perl -pi -e "s#-pthread#-lpthread#g" $RPM_BUILD_ROOT%{_libdir}/lib*.la
perl -pi -e 's#/etc/httpd/build#%{_libexecdir}/build#g' $RPM_BUILD_ROOT%{_libexecdir}/build/*
ln -sf %{_bindir}/libtool $RPM_BUILD_ROOT%{_libexecdir}/build/libtool
ln -sf %{_libexecdir}/build $RPM_BUILD_ROOT%{_sysconfdir}/build

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/apache

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,agent,referer,suexec}_log

%if %{?_without_ssl:0}%{!?_without_ssl:1}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ssl
install %{SOURCE20} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/server.crt
install %{SOURCE21} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/server.key
%endif

CFG="$RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf/"

install %{SOURCE6}  $CFG/10_httpd.conf
install %{SOURCE8}  $CFG/20_mod_vhost_alias.conf
install %{SOURCE9}  $CFG/25_mod_status.conf
install %{SOURCE10} $CFG/30_mod_proxy.conf
install %{SOURCE11} $CFG/35_mod_info.conf
install %{SOURCE12} $CFG/40_mod_ssl.conf
install %{SOURCE13} $CFG/45_mod_dav.conf
install %{SOURCE14} $CFG/59_mod_dir.conf

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
echo "LoadModule expires_module       %{_libexecdir}/mod_expires.so" > $CFG/60_mod_expires.conf
echo "LoadModule file_cache_module    %{_libexecdir}/mod_file_cache.so" > $CFG/61_mod_file_cache.conf
echo "LoadModule headers_module       %{_libexecdir}/mod_headers.so" > $CFG/62_mod_headers.conf
echo "LoadModule imap_module          %{_libexecdir}/mod_imap.so" > $CFG/63_mod_imap.conf
echo "LoadModule rewrite_module       %{_libexecdir}/mod_rewrite.so" > $CFG/64_mod_rewrite.conf
echo "LoadModule usertrack_module     %{_libexecdir}/mod_usertrack.so" > $CFG/65_mod_usertrack.conf
echo "LoadModule unique_id_module     %{_libexecdir}/mod_unique_id.so" > $CFG/66_mod_unique_id.conf

ln -sf index.html.en $RPM_BUILD_ROOT%{_datadir}/html/index.html

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid http`" ]; then
	if [ "`getgid http`" != "51" ]; then
		echo "Error: group http doesn't have gid=51. Correct this before installing apache." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 51 -r -f http
fi
if [ -n "`id -u http 2>/dev/null`" ]; then
	if [ "`id -u http`" != "51" ]; then
		echo "Error: user http doesn't have uid=51. Correct this before installing apache." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 51 -r -d /home/services/httpd -s /bin/false -c "HTTP User" -g http http 1>&2
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

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE CHANGES README
%doc docs/conf/mime.types

%attr(754,root,root) /etc/rc.d/init.d/httpd

%attr(750,root,root) %dir %{_sysconfdir}
%attr(750,root,root) %dir %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_httpd.conf
%attr(640,root,root) %{_sysconfdir}/magic
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

# look at TODO on top
%attr(755,root,root) %{_libexecdir}/mod_case_filter.so
%attr(755,root,root) %{_libexecdir}/mod_case_filter_in.so
%attr(755,root,root) %{_libexecdir}/mod_echo.so
%attr(755,root,root) %{_libexecdir}/mod_ext_filter.so
%attr(755,root,root) %{_libexecdir}/mod_optional_fn_export.so
%attr(755,root,root) %{_libexecdir}/mod_optional_fn_import.so
%attr(755,root,root) %{_libexecdir}/mod_optional_hook_export.so
%attr(755,root,root) %{_libexecdir}/mod_optional_hook_import.so

%attr(755,root,root) %{_sbindir}/htdigest

%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/checkgid
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs
%attr(755,root,root) %{_sbindir}/envvars*

%dir %attr(770,root,http) /var/run/apache

%{_mandir}/man1/htdigest.1*
%{_mandir}/man8/*

%attr(750,root,root) %dir /var/log/httpd
%attr(750,root,root) %dir /var/log/archiv/httpd
%attr(640,root,root) %ghost /var/log/httpd/*

%dir %{_datadir}
%dir %{_datadir}/manual
%{_datadir}/manual/LICENSE
%{_datadir}/manual/*.xml
%{_datadir}/manual/*.html.en
%lang(ja) %{_datadir}/manual/*.html.ja.jis
%lang(ja) %{_datadir}/manual/*.xml.ja
%lang(ko) %{_datadir}/manual/*.html.ko.euc-kr
%lang(de) %{_datadir}/manual/*.html.de
%lang(fr) %{_datadir}/manual/*.html.fr
%{_datadir}/manual/developer
%{_datadir}/manual/faq
%dir %{_datadir}/manual/howto
%doc %{_datadir}/manual/howto/*.en
%lang(ja) %{_datadir}/manual/howto/*.ja.jis
%dir %{_datadir}/manual/images
%{_datadir}/manual/images/[achips]*
%{_datadir}/manual/misc
%dir %{_datadir}/manual/mod
%{_datadir}/manual/mod/[cdfhipw]*.html.en
%{_datadir}/manual/mod/[acd]*.xml
%lang(ja) %{_datadir}/manual/mod/[ad]*.xml.ja*
%lang(ja) %{_datadir}/manual/mod/index.html.ja.jis
%lang(ja) %{_datadir}/manual/mod/index.xml.ja
%{_datadir}/manual/mod/index.xml
%{_datadir}/manual/mod/mpm*.html.en
%{_datadir}/manual/mod/mod_access.html.en
%{_datadir}/manual/mod/mod_alias.html.en
%{_datadir}/manual/mod/mod_asis.html.en
%{_datadir}/manual/mod/mod_autoindex.html.en
%{_datadir}/manual/mod/mod_cern_meta.html.en
%{_datadir}/manual/mod/mod_cgi.html.en
%{_datadir}/manual/mod/mod_env.html.en
%{_datadir}/manual/mod/mod_include.html.en
%{_datadir}/manual/mod/mod_log_config.html.en
%{_datadir}/manual/mod/mod_mime*.html.en
%{_datadir}/manual/mod/mod_negotiation.html.en
%{_datadir}/manual/mod/mod_setenvif.html.en
%{_datadir}/manual/mod/mod_speling.html.en
%{_datadir}/manual/mod/mod_userdir.html.en
%{_datadir}/manual/platform
%{_datadir}/manual/programs
%dir %{_datadir}/manual/search
%doc%attr(755,root,root) %{_datadir}/manual/search/manual-index.cgi
%{_datadir}/manual/style

%attr(755,root,root) %dir %{_datadir}/html
%{_datadir}/icons
%attr(755,root,root) %{_datadir}/cgi-bin

%{_datadir}/error

%files suexec
%defattr(644,root,root,755)
%attr(4755,root,root) %{_sbindir}/suexec
%attr(755,root,root) %{_libexecdir}/mod_suexec.so
%{_datadir}/manual/mod/mod_suexec.html.en

%files index
%defattr(644,root,root,755)
%config(noreplace,missingok) %{_datadir}/html/index.html*
%{_datadir}/html/*.gif
%{_datadir}/html/*.png

%files devel
%defattr(644,root,root,755)
%{_includedir}
%{_libexecdir}/*.exp
%attr(755,root,root) %dir %{_libexecdir}/build
%attr(644,root,root) %{_libexecdir}/build/*.mk
%attr(755,root,root) %{_libexecdir}/build/*.sh
%attr(755,root,root) %{_libexecdir}/build/libtool

%files mod_actions
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_actions.conf
%attr(755,root,root) %{_libexecdir}/mod_actions.so
%{_datadir}/manual/mod/mod_actions.html.en

%files mod_auth
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_auth.so
%attr(755,root,root) %{_sbindir}/htpasswd
%{_datadir}/manual/mod/mod_auth.html.en
%{_mandir}/man1/htpasswd.1*

%files mod_auth_anon
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_auth_anon.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_anon.so
%{_datadir}/manual/mod/mod_auth_anon.html.en

%files mod_auth_dbm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_auth_dbm.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_dbm.so
%attr(755,root,root) %{_sbindir}/dbmmanage
%attr(755,root,root) %{_sbindir}/htdbm
%{_datadir}/manual/mod/mod_auth_dbm.html.en
%{_mandir}/man1/dbmmanage.1*

%files mod_auth_digest
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_auth_digest.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_digest.so
%{_datadir}/manual/mod/mod_auth_digest.html.en

%files mod_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_cache.conf
%attr(755,root,root) %{_libexecdir}/mod_cache.so
%attr(755,root,root) %{_libexecdir}/mod_disk_cache.so
%attr(755,root,root) %{_libexecdir}/mod_mem_cache.so
%{_datadir}/manual/mod/mod_cache.html.en

%files mod_cgid
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_cgid.conf
%attr(755,root,root) %{_libexecdir}/mod_cgid.so
%{_datadir}/manual/mod/mod_cgid.html.en

%files mod_charset_lite
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_charset_lite.conf
%attr(755,root,root) %{_libexecdir}/mod_charset_lite.so
%{_datadir}/manual/mod/mod_charset_lite.html.en

%files mod_dav
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_dav.conf
%attr(755,root,root) %{_libexecdir}/mod_dav*.so
%{_datadir}/manual/mod/mod_dav*.html.en

%files mod_deflate
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_deflate.conf
%attr(755,root,root) %{_libexecdir}/mod_deflate.so
%{_datadir}/manual/mod/mod_deflate.html.en

%files mod_dir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_dir.conf
%attr(755,root,root) %{_libexecdir}/mod_dir.so
%{_datadir}/manual/mod/mod_dir.html.en

%files mod_expires
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_expires.conf
%attr(755,root,root) %{_libexecdir}/mod_expires.so
%{_datadir}/manual/mod/mod_expires.html.en

%files mod_file_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_file_cache.conf
%attr(755,root,root) %{_libexecdir}/mod_file_cache.so
%{_datadir}/manual/mod/mod_file_cache.html.en

%files mod_headers
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_headers.conf
%attr(755,root,root) %{_libexecdir}/mod_headers.so
%{_datadir}/manual/mod/mod_headers.html.en

%files mod_imap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_imap.conf
%attr(755,root,root) %{_libexecdir}/mod_imap.so
%{_datadir}/manual/mod/mod_imap.html.en

%files mod_info
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_info.conf
%attr(755,root,root) %{_libexecdir}/mod_info.so
%{_datadir}/manual/mod/mod_info.html.en

%files mod_proxy
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_proxy.conf
%attr(755,root,root) %{_libexecdir}/mod_proxy*.so
%doc %{_datadir}/manual/mod/mod_proxy*.html.en
%attr(770,root,http) /var/cache/apache

%files mod_rewrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_rewrite.conf
%{_datadir}/manual/mod/mod_rewrite.html.en
%{_datadir}/manual/images/mod_rewrite*

%if %{!?_without_ssl:1}%{?_without_ssl:0}
%files mod_ssl
%defattr(644,root,root,755)
%attr(750,root,root) %dir %{_sysconfdir}/ssl
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ssl/server.*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_ssl.conf
%attr(755,root,root) %{_libexecdir}/mod_ssl.so
%{_datadir}/manual/ssl
%{_datadir}/manual/mod/mod_ssl.html.en
%endif

%files mod_status
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_status.conf
%attr(755,root,root) %{_libexecdir}/mod_status.so
%{_datadir}/manual/mod/mod_status.html.en

%files mod_usertrack
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_usertrack.conf
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so
%{_datadir}/manual/mod/mod_usertrack.html.en

%files mod_unique_id
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_unique_id.conf
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so
%{_datadir}/manual/mod/mod_unique_id.html.en

%files mod_vhost_alias
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
%{_datadir}/manual/mod/mod_vhost_alias.html.en
%{_datadir}/manual/vhosts
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf/*_mod_vhost_alias.conf

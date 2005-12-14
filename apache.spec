# TODO:
# - distcache.spec
# - mod_case_filter
# - mod_case_filter_in
# - mod_optional_fn_{export,import}
# - mod_optional_hook_{export,import}
# - mod_ext_filter
# - mod_echo
# - config examples for mod_*
# - find smart way to deregister module if its moved from main package
#   to subpackage (maybe test -f ?)
# - add %%post/%%postun to suexec
# - --with-suexec-gidmin=500 or =100 ?
# - --with-suexec-uidmin=500 or =1000 ?
# - subpackages for MPMs
# - check if all modules (*.so) are exactly the same for different MPMs
# - install stage fails with distcc (make -jN)
# - /var/run/apache is also owned by apache1.spec, so rename it to /var/run/httpd spec here (NOTE: if you fix this also adjust apache-mod_fastcgi.spec)
#

# Conditional build:
%bcond_without	ssl		# build without SSL support
%bcond_without	ldap		# build without LDAP support
%bcond_without	metuxmpm
%bcond_without	peruser
%bcond_without	event
%bcond_with     distcache
%bcond_with	bucketeer	# debug one
#
%include	/usr/lib/rpm/macros.perl
# this is internal macro, don't change to %%apache_modules_api
%define		_apache_modules_api 20051115
Summary:	The most widely used Web server on the Internet
Summary(de):	Leading World Wide Web-Server
Summary(es):	Servidor HTTPD para proveer servicios WWW
Summary(fr):	Le serveur web le plus utilise sur Internet
Summary(pl):	Serwer WWW (World Wide Web)
Summary(pt_BR):	Servidor HTTPD para prover serviços WWW
Summary(ru):	óÁÍÙÊ ÐÏÐÕÌÑÒÎÙÊ ×ÅÂ-ÓÅÒ×ÅÒ
Summary(tr):	Lider WWW tarayýcý
Name:		apache
Version:	2.2.0
Release:	0.3
License:	Apache Group License
Group:		Networking/Daemons
Source0:	http://www.apache.org/dist/httpd/httpd-%{version}.tar.gz
# Source0-md5:	760aecf26a071e15141170636af43456
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	%{name}-icons.tar.gz
# Source3-md5:	2b085cbc19fd28536dc883f0b864cd83
Source4:	%{name}.sysconfig
Source5:	%{name}.monitrc
Source6:	%{name}-httpd.conf
Source8:	%{name}-mod_vhost_alias.conf
Source9:	%{name}-mod_status.conf
Source10:	%{name}-mod_proxy.conf
Source11:	%{name}-mod_info.conf
Source12:	%{name}-mod_ssl.conf
Source13:	%{name}-mod_dav.conf
Source14:	%{name}-mod_dir.conf
Source15:	%{name}-mod_suexec.conf
Source16:	%{name}-mod_deflate.conf
Source17:	%{name}-mod_autoindex.conf
Source20:	%{name}-server.crt
Source21:	%{name}-server.key
Patch0:		%{name}-configdir_skip_backups.patch
Patch1:		%{name}-layout.patch
Patch2:		%{name}-suexec.patch
Patch4:		%{name}-apr.patch
# project homepage http://www.metux.de/mpm/en/?patpage=index
# http://www.sannes.org/metuxmpm/
Patch5:		httpd-2.0.48-metuxmpm-r8.patch
# what about this? it isn't applied...
Patch6:		httpd-2.0.40-xfsz.patch
Patch8:		httpd-2.0.45-encode.patch
Patch10:	httpd-2.0.46-dav401dest.patch
Patch12:	httpd-2.0.46-sslmutex.patch
Patch14:	httpd-2.0.48-corelimit.patch
Patch15:	httpd-2.0.48-debuglog.patch
Patch18:	%{name}-v6only-ENOPROTOOPT.patch
Patch19:	%{name}-conffile-path.patch
Patch20:	%{name}-apxs.patch
# http://www.telana.com/peruser.php
Patch21:	httpd-2.0.52-peruser-0.1.6.patch
Patch22:	%{name}-libtool.patch
URL:		http://httpd.apache.org/
BuildRequires:	apr-devel >= 1:1.0.0
BuildRequires:	apr-util-devel >= 1:1.0.0
BuildRequires:	automake
BuildRequires:	db-devel
%{?with_distcache:BuildRequires:	distcache-libs-devel or distcache-devel}
BuildRequires:	expat-devel
BuildRequires:	findutils
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	libtool >= 2:1.5
%{?with_ldap:BuildRequires:	openldap-devel}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_ssl:BuildRequires:	openssl-tools >= 0.9.7d}
BuildRequires:	pcre-devel
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	zlib-devel
Requires(post):	fileutils
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	/etc/mime.types
Requires:	/sbin/chkconfig
Requires:	apr >= 1:1.0.0-2
Requires:	mailcap
Requires:	perl-base
Requires:	psmisc >= 20.1
Requires:	rc-scripts >= 0.4.0.15
Provides:	apache(modules-api) = %{_apache_modules_api}
#Provides:	apache(mod_access)
Provides:	apache(mod_alias)
Provides:	apache(mod_asis)
Provides:	apache(mod_autoindex)
Provides:	apache(mod_cern_meta)
Provides:	apache(mod_cgi)
Provides:	apache(mod_env)
Provides:	apache(mod_include)
Provides:	apache(mod_log_config)
Provides:	apache(mod_mime)
Provides:	apache(mod_mime_magic)
Provides:	apache(mod_negotiation)
Provides:	apache(mod_setenvif)
Provides:	apache(mod_speling)
Provides:	apache(mod_userdir)
Provides:	group(http)
Provides:	httpd = %{version}
Provides:	user(http)
Provides:	webserver = apache
Obsoletes:	apache-extra
Obsoletes:	apache6
# for the posttrans scriptlet, conflicts because in vserver environment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/httpd
%define		_includedir	%{_prefix}/include/apache
%define		_datadir	/home/services/httpd
%define		_libexecdir	%{_libdir}/apache
%define		_cgibindir	%{_prefix}/lib/cgi-bin/%{name}

%description
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%description -l de
Apache ist ein voll funktionsfähiger Web-Server, der kostenlos
erhältlich und weit verbreitet ist.

%description -l es
El servidor web Apache es el mejor servidor gratuito disponible en el
mundo UNIX hoy. Usa HTTP (HyperText Transfer Protocol) para permitir
que navegadores vean documentos y sometan datos remotamente. Puede
ejecutar varias funciones diferentes, incluyendo funciones de proxy y
caché, y nos ofrece características como monitor de estado, conversión
dinámica de tipo, y otras más.

%description -l fr
Apache est un serveur Web puissant, efficace, gratuit et complet.
Apache est aussi le serveur Web le plus populaire sur Internet.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj±c ten pakiet
bêdziesz móg³ prezentowaæ w³asne strony WWW w sieci Internet.

%description -l pt_BR
O servidor web Apache é o melhor servidor gratuito disponível no mundo
UNIX hoje. Ele usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vejam documentos e submetam dados remotamente. Ele
pode executar várias funções diferentes, incluindo funções de proxy e
cache, e oferece características como monitor de status, conversão
dinâmica de tipo, e mais.

%description -l ru
Apache - ÍÏÝÎÙÊ, ÆÕÎËÃÉÏÎÁÌØÎÙÊ, ×ÙÓÏËÏÐÒÏÉÚ×ÏÄÉÔÅÌØÎÙÊ É Ó×ÏÂÏÄÎÏ
ÒÁÓÐÒÏÓÔÒÁÎÑÅÍÙÊ ×ÅÂ-ÓÅÒ×ÅÒ.

%description -l tr
Apache serbest daðýtýlan ve çok kullanýlan yetenekli bir web
sunucusudur.

%package suexec
Summary:	Apache suexec wrapper
Summary(pl):	Wrapper suexec do serwera WWW Apache
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and
SSI programs under user IDs different from the user ID of the calling
web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description suexec -l pl
SuEXEC umo¿liwia serwerowi Apache uruchamianie programów CGI i SSI z
innym UID ni¿ wywo³uj±cy je serwer. Normalnie programy CGI i SSI s±
wykonywane jako taki sam u¿ytkownik jak serwer WWW.

%package index
Summary:	Apache index.html* files
Summary(pl):	Pliki Apache index.html*
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Obsoletes:	indexhtml

%description index
Apache index.html* files.

%description index -l pl
Pliki index.html* Apache'a.

%package doc
Summary:	Apache manual
Summary(pl):	Podrêcznik Apache'a
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Apache manual.

%description doc -l pl
Podrêcznik Apache'a.

%package apxs
Summary:	APache eXtenSion tool
Summary(pl):	Narzêdzie do rozszerzania Apache'a
Group:		Development/Tools

%description apxs
APache eXtenSion tool.

%description apxs -l pl
Narzêdzie do rozszerzania Apache'a.

%package devel
Summary:	Module development tools for the Apache web server
Summary(es):	Archivos de inclusión del Apache para desarrollo de módulos
Summary(fr):	Les outils de developpement de modules pour le serveur web Apache
Summary(pl):	Pliki nag³ówkowe do tworzenia modu³ów rozszerzeñ do serwera WWW Apache
Summary(pt_BR):	Arquivos de inclusão do Apache para desenvolvimento de módulos
Summary(ru):	óÒÅÄÓÔ×Á ÒÁÚÒÁÂÏÔËÉ ÍÏÄÕÌÅÊ ÄÌÑ ×ÅÂ-ÓÅÒ×ÅÒÁ Apache
Group:		Networking/Utilities
Requires:	%{name}-apxs = %{version}-%{release}
Requires:	apr-util-devel >= 1:1.0.0
Requires:	libtool
Obsoletes:	apache-static

%description devel
The apache-devel package contains header files for Apache.

%description devel -l es
Este paquete contiene los archivos de inclusión para el Apache, bien
como el utilitario apxs para la construcción de objetos compartidos
dinámicos (DSOs). Ha ce falta instalar este paquete si deseas compilar
o desarrollar módulos adicionales para Apache.

%description devel -l fr
Le package apache-devel contient le code source pour le serveur Web
Apache et le binaire APXS dont vous aurez besoin pour construire des
Objets Dynamiques Partages (DSOs) pour Apache.

%description devel -l pl
Pliki nag³ówkowe i inne zasoby niezbêdne przy budowaniu modu³ów DSO
(Dynamic Shared Objects) dla Apache'a.

%description devel -l ru
óÒÅÄÓÔ×Á ÒÁÚÒÁÂÏÔËÉ ÍÏÄÕÌÅÊ ÄÌÑ ×ÅÂ-ÓÅÒ×ÅÒÁ Apache.

%description devel -l pt_BR
Este pacote contem os arquivos de inclusão para o Apache, bem como o
utilitário apxs para a construção de objetos compartilhados dinâmicos
(DSOs). Este pacote precisa ser instalado se você deseja compilar ou
desenvolver módulos adicionais para o Apache.

%package mod_actions
Summary:	Apache module for run CGI whenever a file of a certain type is requested
Summary(pl):	Modu³ Apache'a do uruchamiania skryptów CGI
Group:		Networking/Daemons
Provides:	apache(mod_actions) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_actions
This package contains mod_actions module. This module lets you run CGI
scripts whenever a file of a certain type is requested. This makes it
much easier to execute scripts that process files.

%description mod_actions -l pl
Ten modu³ pozwala na uruchamianie skryptów w momencie gdy nadchodzi
¿±danie pobrania pliku okre¶lonego typu.

%package mod_auth
Summary:	Virtual package which which provides backward compat with apache 2.0
Group:		Networking/Daemons
Provides:	apache(mod_auth) = %{version}-%{release}
Requires:	%{name}-mod_authn_file = %{version}-%{release}
Requires:	%{name}-mod_authz_groupfile = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_auth
Virtual package which which requires apache-mod_authn_file and
apache-mod_authz_groupfile for backward compatibility with apache 2.0.

%package mod_auth_basic
Summary:	Apache module that allows basic authentication
Group:		Networking/Daemons
Provides:	apache(mod_auth_basic) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_auth_basic
This module allows the use of HTTP Basic Authentication to restrict
access by looking up users in the given providers.

%package mod_auth_dbm
Summary:	Virtual package which which provides backward compat with apache 2.0
Group:		Networking/Daemons
Provides:	apache(mod_auth_dbm) = %{version}-%{release}
Requires:	%{name}-dbmtools = %{version}-%{release}
Requires:	%{name}-mod_authn_dbm = %{version}-%{release}
Requires:	%{name}-mod_authz_dbm = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_auth_dbm
Virtual package which which requires apache-mod_authn_dbm and
apache-mod_authz_dbm for backward compatibility with apache 2.0.

%package mod_auth_digest
Summary:	User authentication using MD5 Digest Authentication
Group:		Networking/Daemons
Provides:	apache(mod_auth_digest) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_auth_digest
This module implements HTTP Digest Authentication. However, it has not
been extensively tested and is therefore marked experimental.

%package mod_authn_alias
Summary:	Apache module that provides the ability to create extended authentication
Group:		Networking/Daemons
Provides:	apache(mod_authn_alias) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authn_alias
This module allows extended authentication providers to be created
within the configuration file and assigned an alias name.

%package mod_authn_anon
Summary:	Apache module that allows "anonymous" user access to authenticated areas
Group:		Networking/Daemons
Provides:	apache(mod_authn_anon) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
# compat
Provides:	apache-mod_auth_anon = %{version}-%{release}
Provides:	apache(mod_auth_anon) = %{version}-%{release}
Obsoletes:	apache-mod_auth_anon < 2.2.0

%description mod_authn_anon
This module provides authentication front-ends such as mod_auth_basic
to authenticate users similar to anonymous-ftp sites, i.e. have a
'magic' user id 'anonymous' and the email address as a password. These
email addresses can be logged.

%package mod_authn_dbd
Summary:	Apache module that allows user authentication using an SQL
Group:		Networking/Daemons
Provides:	apache(mod_authn_dbd) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authn_dbd
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in SQL
tables.

%package mod_authn_dbm
Summary:	Apache module that allows user authentication using DBM files
Group:		Networking/Daemons
Provides:	apache(mod_authn_dbm) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authn_dbm
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in dbm
password files.

%package mod_authn_default
Summary:	Apache module that rejects any credentials supplied by the user
Group:		Networking/Daemons
Provides:	apache(mod_authn_default) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authn_default
This module is designed to be the fallback module, if you don't have
configured an authentication module like mod_auth_basic. It simply
rejects any credentials supplied by the user.

%package mod_authn_file
Summary:	Apache module that allows user authentication using text files
Group:		Networking/Daemons
Provides:	apache(mod_authn_file) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authn_file
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in plain
text password files.

%package mod_authnz_ldap
Summary:	Apache module that allows an LDAP directory to be used to store the database for HTTP Basic authentication
Group:		Networking/Daemons
Provides:	apache(mod_authnz_ldap) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
# compat
Provides:	apache(mod_auth_ldap) = %{version}-%{release}
Provides:	apache-mod_auth_ldap = %{version}-%{release}
Obsoletes:	apache-mod_auth_ldap < 2.2.0

%description mod_authnz_ldap
This module provides authentication front-ends such as mod_auth_basic
to authenticate users through an ldap directory.

%package mod_authz_dbm
Summary:	Apache module that allows group authorization using DBM files
Group:		Networking/Daemons
Provides:	apache(mod_authz_dbm) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authz_dbm
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by
group membership.

%package mod_authz_default
Summary:	Apache module that rejects any authorization request
Group:		Networking/Daemons
Provides:	apache(mod_authz_default) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authz_default
This module is designed to be the fallback module, if you don't have
configured an authorization module like mod_authz_user or
mod_authz_groupfile. It simply rejects any authorization request.

%package mod_authz_groupfile
Summary:	Apache module that allows group authorization using plaintext files
Group:		Networking/Daemons
Provides:	apache(mod_authz_groupfile) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authz_groupfile
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by
group membership.

%package mod_authz_host
Summary:	Apache module that allows group authorizations based on host (name or IP address) group authorization using plaintext files
Group:		Networking/Daemons
Provides:	apache(mod_authz_host) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authz_host
The directives provided by mod_authz_host are used in <Directory>,
<Files>, and <Location> sections as well as .htaccess files to control
access to particular parts of the server. Access can be controlled
based on the client hostname, IP address, or other characteristics of
the client request, as captured in environment variables.

%package mod_authz_owner
Summary:	Apache module that allows authorization based on file ownership
Group:		Networking/Daemons
Provides:	apache(mod_authz_owner) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authz_owner
This module authorizes access to files by comparing the userid used
for HTTP authentication (the web userid) with the file-system owner or
group of the requested file. The supplied username and password must
be already properly verified by an authentication module, such as
mod_auth_basic or mod_auth_digest.

%package mod_authz_user
Summary:	Apache module that allows user authorization
Group:		Networking/Daemons
Provides:	apache(mod_authz_user) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_authz_user
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site.

%package mod_autoindex
Summary:	Apache module - display index of files
Summary(pl):	Modu³ apache do wy¶wietlania indeksu plików
Group:		Networking/Daemons
Provides:	apache(mod_autoindex) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_autoindex
This package contains mod_autoindex module. It provides generation
index of files.

%description mod_autoindex -l pl
Ten pakiet dostarcza modu³ autoindex, który generuje indeks plików.

%package mod_bucketeer
Summary:	Split buckets whenever we find a control-char
Group:		Networking/Daemons
Provides:	apache(mod_bucketeer) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_bucketeer
Split buckets whenever we find a control-char.

%package mod_cache
Summary:	Content cache keyed to URIs
Summary(pl):	Pamiêæ podrêczna wg klucza URI
Group:		Networking/Daemons
Provides:	apache(mod_cache) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_cache
mod_cache implements an RFC 2616 compliant HTTP content cache that can
be used to cache either local or proxied content. Two storage
management modules are included in the base Apache distribution:
mod_disk_cache implements a disk based storage manager (generally used
for proxy caching) and mod_mem_cache implements an in-memory based
storage manager (primarily useful for caching local content).

%description mod_cache -l pl
Implementacja zgodnej z RFC 2616 pamiêci podrêcznej, która mo¿e byæ
u¿ywana do zapamiêtywania zawarto¶ci lokalnej lub dostêpnej przez
proxy. Do³±czono dwa modu³y pozwalaj±ce magazynowaæ dane w pamiêci
(g³ównie u¿yteczne przy cache'owaniu lokalnej zawarto¶ci) oraz na
dysku (u¿ywane do cache'owania proxy).

%package mod_cgid
Summary:	Execution of CGI scripts using an external CGI daemon
Summary(pl):	Uruchamianie zewnêtrznych skryptów CGI za pomoc± daemona CGI
Group:		Networking/Daemons
Provides:	apache(mod_cgid) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_cgid
Execution of CGI scripts using an external CGI daemon.

%description mod_cgid -l pl
Uruchamianie zewnêtrznych skryptów CGI za pomoc± demona CGI.

%package mod_charset_lite
Summary:	Specify character set translation or recoding
Summary(pl):	Translacja lub przekodowywanie znaków
Group:		Networking/Daemons
Provides:	apache(mod_charset_lite) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_charset_lite
Specify character set translation or recoding.

%description mod_charset_lite -l pl
Translacja lub przekodowywanie znaków.

%package mod_dav
Summary:	Apache module - Distributed Authoring and Versioning
Summary(pl):	Modu³ Apache'a - rozproszone autorstwo i wersjonowanie
Group:		Networking/Daemons
Provides:	apache(mod_dav) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_dav
This module provides class 1 and class 2 WebDAV ('Web-based
Distributed Authoring and Versioning') functionality for Apache. This
extension to the HTTP protocol allows creating, moving, copying, and
deleting resources and collections on a remote web server.

%description mod_dav -l pl
Modu³ udostêpnia klasê 1 oraz klasê 2 WebDAV (Bazuj±cego na WWW
rozproszonego autorstwa i wersjonowania). To rozszerzenie HTTP pozwala
na tworzenie, przesuwanie, kopiowanie oraz kasowanie zasobów na
zdalnym serwerze WWW.

%package mod_dbd
Summary:	Manages SQL database connections
Group:		Networking/Daemons
Provides:	apache(mod_dbd) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_dbd
mod_dbd manages SQL database connections using apr_dbd. It provides
database connections on request to modules requiring SQL database
functions, and takes care of managing databases with optimal
efficiency and scalability for both threaded and non-threaded MPMs.

%package mod_deflate
Summary:	Apache module: Compress content before it is delivered to the client
Summary(pl):	Modu³ Apache'a kompresuj±cy dane przed przes³aniem ich do klienta
Group:		Networking/Daemons
Provides:	apache(mod_deflate) = %{version}-%{release}
Requires:	%{name}-mod_headers = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_deflate
Compress content before it is delivered to the client.

%description mod_deflate -l pl
Modu³ kompresuj±cy dane przed przes³aniem ich do klienta.

%package mod_dir
Summary:	Apache module for "trailing slash" redirects and serving directory index files
Summary(pl):	Modu³ Apache'a oferuj±cy przekierowania i udostêpnianie informacji o zawarto¶ci katalogu
Group:		Networking/Daemons
Provides:	apache(mod_dir) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_dir
This package contains mod_dir which provides "trailing slash"
redirects and serving directory index files.

%description mod_dir -l pl
Modu³ oferuj±cy przekierowania i udostêpnianie informacji o zawarto¶ci
katalogu.

%package mod_dumpio
Summary:	Dumps all I/O to error log as desired
Group:		Networking/Daemons
Provides:	apache(mod_dumpio) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_dumpio
mod_dumpio allows for the logging of all input received by Apache
and/or all output sent by Apache to be logged (dumped) to the
error.log file.

The data logging is done right after SSL decoding (for input) and
right before SSL encoding (for output). As can be expected, this can
produce extreme volumes of data, and should only be used when
debugging problems.

%package mod_expires
Summary:	Apache module which generates Expires HTTP headers
Summary(pl):	Modu³ Apache'a generuj±cy nag³ówki HTTP Expires
Group:		Networking/Daemons
Provides:	apache(mod_expires) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_expires
This module controls the setting of the Expires HTTP header in server
responses. The expiration date can set to be relative to either the
time the source file was last modified, or to the time of the client
access.

%description mod_expires -l pl
Modu³ kontroluje ustawianie nag³ówka HTTP Expires. Data wyga¶niêcia
wa¿no¶ci mo¿e byæ ustalana w zale¿no¶ci od czasu modyfikacji plików
¼ród³owych lub odwo³ania klienta.

%package mod_file_cache
Summary:	Apache module: caches a static list of files in memory
Summary(pl):	Modu³ Apache'a cache'uj±cy statyczn± listê plików w pamiêci
Group:		Networking/Daemons
Obsoletes:	apache-mmap_static
Provides:	apache(mod_file_cache) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_file_cache
Caches a static list of files in memory.

%description mod_file_cache -l pl
Modu³ cache'uj±cy statyczn± listê plików w pamiêci.

%package mod_filter
Summary:	Context-sensitive smart filter configuration module
Group:		Networking/Daemons
Provides:	apache(mod_filter) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_filter
This module enables smart, context-sensitive configuration of output
content filters. For example, apache can be configured to process
different content-types through different filters, even when the
content-type is not known in advance (e.g. in a proxy).

%package mod_headers
Summary:	Apache module allows for the customization of HTTP response headers
Summary(pl):	Modu³ Apache'a pozwalaj±cy na modyfikacjê nag³ówków HTTP
Group:		Networking/Daemons
Provides:	apache(mod_headers) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_headers
This package contains mod_headers module. The module allows for the
customization of HTTP response headers. Headers can be merged,
replaced or removed.

%description mod_headers -l pl
Modu³ pozwalaj±cy na ³±czenie, usuwanie oraz zamianê nag³ówków HTTP
wysy³anych do przegl±darki.

%package mod_ident
Summary:	RFC 1413 ident lookups
Group:		Networking/Daemons
Provides:	apache(mod_ident) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_ident
This module queries an RFC 1413 compatible daemon on a remote host to
look up the owner of a connection.

%package mod_imagemap
Summary:	Server-side imagemap processing
Group:		Networking/Daemons
Provides:	apache(mod_imagemap) = %{version}-%{release}
Obsoletes:	%{name}-mod_imap
Requires:	%{name} = %{version}-%{release}

%description mod_imagemap
This module processes .map files, thereby replacing the functionality
of the imagemap CGI program. Any directory or document type configured
to use the handler imap-file (using either AddHandler or SetHandler)
will be processed by this module.

%package mod_imap
Summary:	Apache module with imap-file handler
Summary(pl):	Modu³ Apache'a z obs³ug± imap-file
Group:		Networking/Daemons
Provides:	apache(mod_imap) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_imap
This package contains mod_imap module. It provides for .map files,
replacing the functionality of the imagemap CGI program. Any directory
or document type configured to use the handler imap-file.

%description mod_imap -l pl
Modu³ umo¿liwiaj±cy obs³ugê plików .map (imap-file handler).

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Summary(pl):	Modu³ Apache'a udostêpniaj±cy informacje o serwerze
Group:		Networking/Daemons
Provides:	apache(mod_info) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_info
This package contains mod_info module. It provides a comprehensive
overview of the server configuration including all installed modules
and directives in the configuration files.

%description mod_info -l pl
Modu³ udostêpniaj±cy informacje o konfiguracji serwera,
zainstalowanych modu³ach itp.

%package mod_ldap
Summary:	Apache module to use LDAP connections
Summary(pl):	Modu³ Apache'a umo¿liwiaj±cy korzystanie z po³±czeñ LDAP
Group:		Networking/Daemons
Provides:	apache(mod_ldap) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_ldap
Apache module to use LDAP connections.

%description mod_ldap -l pl
Modu³ Apache'a umo¿liwiaj±cy korzystanie z po³±czeñ LDAP.

%package mod_logio
Summary:	Logging of input and output bytes per request
Group:		Networking/Daemons
Provides:	apache(mod_logio) = %{version}-%{release}
#Requires:	%{name}-mod_log_config = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_logio
This module provides the logging of input and output number of bytes
received/sent per request. The numbers reflect the actual bytes as
received on the network, which then takes into account the headers and
bodies of requests and responses. The counting is done before SSL/TLS
on input and after SSL/TLS on output, so the numbers will correctly
reflect any changes made by encryption.

%package mod_proxy
Summary:	Apache module with Web proxy
Summary(pl):	Modu³ Apache'a dodaj±cy obs³ugê serwera proxy
Group:		Networking/Daemons
Provides:	apache(mod_proxy) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_proxy
This package contains module with implementation a proxy/cache for
Apache. It implements proxying capability for FTP, CONNECT (for SSL),
HTTP/0.9, HTTP/1.0 and HTTP/1.1. The module can be configured to
connect to other proxy modules for these and other protocols.

%description mod_proxy -l pl
Modu³ zawiera implementacjê serwera proxy/cache dla Apache.
Implementacja zawiera obs³ugê FTP, CONNECT (dla SSL), HTTP/0.9,
HTTP/1.0 i HTTP/1.1.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Summary(pl):	Modu³ Apache'a do "przepisywania" adresów URL w locie
Group:		Networking/Daemons
Provides:	apache(mod_rewrite) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to
rewrite requested URLs on the fly.

%description mod_rewrite -l pl
Modu³ oferuj±cy mo¿liwo¶æ "przepisywania" adresów URL w locie.

%package mod_ssl
Summary:	SSL/TLS module for the Apache HTTP server
Summary(pl):	Modu³ SSL/TSL dla serwera Apache
Summary(ru):	íÏÄÕÌØ SSL/TLS ÄÌÑ ×ÅÂ-ÓÅÒ×ÅÒÁ Apache
Group:		Networking/Daemons
Epoch:		1
Provides:	apache(mod_ssl) = 1:%{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer Security
(TLS) protocols.

%description mod_ssl -l pl
Modu³ mod_ssl udostêpnia wsparcie do silnej kryptografii dla serwera
Apache poprzez protoko³y SSL/TSL (Secure Sockets Layer/Transport Layer
Security).

%description mod_ssl -l ru
íÏÄÕÌØ mod_ssl ÏÂÅÓÐÅÞÉ×ÁÅÔ ÐÏÄÄÅÒÖËÕ × ×ÅÂ-ÓÅÒ×ÅÒÅ Apache ÎÁÄÅÖÎÏÇÏ
ÛÉÆÒÏ×ÁÎÉÑ ÓÒÅÄÓÔ×ÁÍÉ Secure Sockets Layer (SSL) É Transport Layer

%package mod_status
Summary:	Server status report module for Apache
Summary(pl):	Modu³ udostêpniaj±cy informacje statystyczne z serwera Apache
Group:		Networking/Daemons
Provides:	apache(mod_status) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_status
The Status module allows a server administrator to find out how well
their server is performing. A HTML page is presented that gives the
current server statistics in an easily readable form. If required this
page can be made to automatically refresh (given a compatible
browser).

%description mod_status -l pl
Modu³ pozwala administratorowi na przegl±danie statystyk dotycz±cych
pracy serwera Apache (w postaci strony HTML).

%package mod_unique_id
Summary:	Apache module which provides a magic token for each request
Summary(pl):	Modu³ Apache'a nadaj±cy ka¿demu zapytaniu unikalny token
Group:		Networking/Daemons
Provides:	apache(mod_unique_id) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_unique_id
This package contains the mod_unique_id. This module provides a magic
token for each request which is guaranteed to be unique across "all"
requests under very specific conditions. The unique identifier is even
unique across multiple machines in a properly configured cluster of
machines. The environment variable UNIQUE_ID is set to the identifier
for each request. Unique identifiers are useful for various reasons
which are beyond the scope of this document.

%description mod_unique_id -l pl
Modu³ nadaje ka¿demu zapytaniu token unikalny w ramach wszystkich
zapytañ, nawet w ramach poprawnie skonfigurowanego klastra z wielu
maszyn. Modu³ ustawia przy ka¿dym zapytaniu zmienn± ¶rodowiskow±
UNIQUE_ID.

%package mod_usertrack
Summary:	Apache module for user tracking using cookies
Summary(pl):	Modu³ Apache'a s³u¿±cy do ¶ledzenia "ciasteczek"
Group:		Networking/Daemons
Provides:	apache(mod_usertrack) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_usertrack
This package contains the user tracking module which did its own
logging using CookieLog directory. This module allow multiple log
files.

%description mod_usertrack -l pl
Modu³ pozwalaj±cy na ¶ledzenie "ciasteczek".

%package mod_version
Summary:	Version dependent configuration
Group:		Networking/Daemons
Provides:	apache(mod_version) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_version
This module is designed for the use in test suites and large networks
which have to deal with different httpd versions and different
configurations. It provides a new container -- <IfVersion>, which
allows a flexible version checking including numeric comparisons and
regular expressions.

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Summary(pl):	Modu³ Apache'a dodaj±cy obs³ugê hostów wirtualnych
Group:		Networking/Daemons
Provides:	apache(mod_vhost_alias) = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

%description mod_vhost_alias -l pl
Modu³ umo¿liwia na dynamiczne konfigurowanie masowej ilo¶ci serwerów
wirtualnych.

%package -n htpasswd-%{name}
Summary:	Apache 2 htpasswd utility: manage user files for basic authentication
Summary(pl):	Narzêdzie htpasswd z Apache'a 2 do zarz±dzania plikami uwierzytelnienia basic
Group:		Networking/Utilities
Provides:	htpasswd
Obsoletes:	htpasswd

%description -n htpasswd-%{name}
htpasswd is used to create and update the flat-files used to store
usernames and password for basic authentication of HTTP users. This
package contains htpasswd from Apache 2; this version supports
plaintext passwords and CRYPT (default), MD5 and SHA1 encryptions.

%description -n htpasswd-%{name} -l pl
htpasswd s³u¿y do tworzenia i uaktualniania plików tekstowych
s³u¿±cych do przechowywania nazw u¿ytkowników i hase³ do podstawowego
uwierzytelnienia u¿ytkowników HTTP. Ten pakiet zawiera htpasswd z
Apache'a 2; ta wersja obs³uguje has³a zapisane czystym tekstem oraz
zakodowane algorytmami CRYPT (domy¶lnym), MD5 i SHA1.

%package dbmtools
Summary:	Apache 2 tools for manipulating DBM files
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description dbmtools
Apache 2 tools for manipulating DBM files.

%package cgi_test
Summary:	cgi test/demo programs
Summary(pl):	Programy testowe/przyk³adowe cgi
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Requires:	FHS >= 2.3-12

%description cgi_test
Two cgi test/demo programs: test-cgi and print-env.

%description cgi_test -l pl
Dwa programy testowe/przyk³adowe cgi: test-cgi and print-env.

%prep
%setup -q -n httpd-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch8 -p1
%patch10 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

# using system apr, apr-util and pcre
rm -rf srclib/{apr,apr-util,pcre}
# nothing left in srclib, remove it
sed -i -e '/^SUBDIRS/s/srclib//' Makefile.in

# fixup perl path
sed -i -e '1s@/usr/local/bin/perl@%{__perl}@' docs/cgi-examples/printenv

# fix location of build dir in generated apxs
sed -i -e '
s:@exp_installbuilddir@:%{_libdir}/apache/build:g
' support/apxs.in

# sanity check
MODULES_API=`awk '/#define MODULE_MAGIC_NUMBER_MAJOR/ {print $3}' include/ap_mmn.h`
if [ "$MODULES_API" != "%_apache_modules_api" ]; then
	echo "Set %%_apache_modules_api to $MODULES_API and rerun."
	exit 1
fi

%build
cp /usr/share/apr/build/apr_common.m4 build
cp /usr/share/libtool/ltmain.sh build
cp /usr/share/automake/config.* build
%{__autoheader}
%{__autoconf}

# from ./buildconf
: fixing timestamps for mod_ssl sources
cd modules/ssl
touch ssl_expr_parse.y
sleep 1
touch ssl_expr_parse.c ssl_expr_parse.h ssl_expr_scan.l
sleep 1
touch ssl_expr_scan.c
cd ../..

CPPFLAGS="-DMAX_SERVER_LIMIT=200000 -DBIG_SECURITY_HOLE=1"
for mpm in %{?with_metuxmpm:metuxmpm} %{?with_peruser:peruser} prefork worker %{?with_event:event}; do
install -d "buildmpm-${mpm}"; cd "buildmpm-${mpm}"
../%configure \
	--prefix=%{_sysconfdir} \
	--exec-prefix=%{_libexecdir} \
	--with-installbuilddir=%{_libdir}/apache/build \
	--disable-v4-mapped \
	--enable-layout=PLD \
	--enable-modules=all \
	--enable-mods-shared=all \
	--enable-auth-anon \
	--enable-auth-dbm \
	--enable-authn-dbd \
	--enable-authn-alias \
	--enable-authz-dbm \
	--enable-authz-owner \
	%{?with_ldap:--enable-authnz-ldap} \
	--enable-auth-digest \
	--enable-file-cache \
	--enable-cache \
	--enable-disk-cache \
	--enable-mem-cache \
	--enable-dbd \
	%{?with_bucketeer:--enable-bucketeer} \
	--enable-dumpio \
	--enable-echo \
	--enable-charset-lite \
	--enable-deflate \
	%{?with_ldap:--enable-ldap} \
	--enable-ext-filter \
	--enable-case-filter \
	--enable-case-filter-in \
	--enable-log-forensic \
	--enable-logio \
	--with-z=%{_prefix} \
	--enable-mime-magic \
	--enable-cern-meta \
	--enable-expires \
	--enable-headers \
	--enable-ident \
	--enable-usertrack \
	--enable-unique-id \
	--enable-proxy \
	--enable-proxy-connect \
	--enable-proxy-ftp \
	--enable-proxy-http \
	--enable-proxy-ajp \
	--enable-proxy-balancer \
	%{?with_ssl:--enable-ssl %{?with_distcache:--enable-distcache}} \
	--enable-optional-hook-export \
	--enable-optional-hook-import \
	--enable-optional-fn-import \
	--enable-optional-fn-export \
	--enable-http \
	--enable-dav \
	--enable-info \
	--enable-suexec \
	--enable-cgi \
	--enable-cgid \
	--enable-dav-fs \
	--enable-dav-lock \
	--enable-vhost-alias \
	--enable-imagemap \
	--enable-speling \
	--enable-rewrite \
	--enable-so \
	--with-program-name=httpd.${mpm} \
	--with-mpm=${mpm} \
%ifarch %{ix86}
%ifnarch i386 i486
	$( [ "${mpm}" = "leader" ] && echo "--enable-nonportable-atomics=yes" ) \
%endif
%endif
	--with-suexec-bin=%{_sbindir}/suexec \
	--with-suexec-caller=http \
	--with-suexec-docroot=%{_datadir} \
	--with-suexec-logfile=/var/log/httpd/suexec_log \
	--with-suexec-uidmin=500 \
	--with-suexec-gidmin=500 \
	--with-suexec-umask=077 \
	--with-apr=%{_bindir}/apr-1-config \
	--with-apr-util=%{_bindir}/apu-1-config \
	--with-pcre

%{__make}
./httpd.${mpm} -l | grep -v "${mpm}" > modules-inside

find include -name '*.h' | xargs perl -pi -e "s#/httpd\.(.*?)\.conf#/etc/httpd/httpd.conf#"

cd ..
done

for mpm in %{?with_metuxmpm:metuxmpm} %{?with_peruser:peruser} worker %{?with_event:event}; do
	if ! cmp -s buildmpm-prefork/modules-inside buildmpm-${mpm}/modules-inside; then
		echo "List of compiled modules is different between prefork-MPM and ${mpm}-MPM!"
		echo "Build failed."
		exit 1
	fi
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig,monit} \
	$RPM_BUILD_ROOT%{_var}/{log/{httpd,archiv/httpd},{run,cache}/apache,lock/mod_dav} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{webapps.d,conf.d} \
	$RPM_BUILD_ROOT%{_datadir}/cgi-bin

# prefork is default one
%{__make} -C buildmpm-prefork install \
	DESTDIR=$RPM_BUILD_ROOT \
	installbuilddir=%{_sysconfdir}/build \
	prefix=%{_sysconfdir}/httpd \
	libexecdir=%{_libdir}/%{name} \
	iconsdir=%{_datadir}/icons \
	errordir=%{_datadir}/error \
	htdocsdir=%{_datadir}/html \
	manualdir=%{_datadir}/manual \
	cgidir=%{_cgibindir} \
	runtimedir=%{_var}/run \
	logdir=%{_var}/log/httpd \
	proxycachedir=%{_var}/cache/httpd

for mpm in %{?with_metuxmpm:metuxmpm} %{?with_peruser:peruser} worker %{?with_event:event}; do
	install buildmpm-${mpm}/httpd.${mpm} $RPM_BUILD_ROOT%{_sbindir}/httpd.${mpm}
	ln -s httpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd.${mpm}.conf
done

ln -s httpd.prefork $RPM_BUILD_ROOT%{_sbindir}/httpd

ln -s %{_libdir}/apache $RPM_BUILD_ROOT%{_sysconfdir}/modules
ln -s %{_localstatedir}/run/apache $RPM_BUILD_ROOT%{_sysconfdir}/run
ln -s %{_libdir}/apache/build $RPM_BUILD_ROOT%{_sysconfdir}/build

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -d $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/build \
	$RPM_BUILD_ROOT%{_libexecdir}/build

%{__perl} -pi -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{_libexecdir}/build/*
%{__perl} -pi -e "s#$RPM_BUILD_DIR#%{_usrsrc}#g" $RPM_BUILD_ROOT%{_libexecdir}/build/*
%{__perl} -pi -e "s#-pthread#-lpthread#g" $RPM_BUILD_ROOT%{_libdir}/lib*.la
%{__perl} -pi -e 's#/etc/httpd/build#%{_libexecdir}/build#g' $RPM_BUILD_ROOT%{_libexecdir}/build/*
ln -sf %{_bindir}/libtool $RPM_BUILD_ROOT%{_libexecdir}/build/libtool
ln -sf %{_libexecdir}/build $RPM_BUILD_ROOT%{_sysconfdir}/build

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/httpd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/monit/httpd.monitrc

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,agent,referer,suexec}_log

%if %{with ssl}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ssl
install %{SOURCE20} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/server.crt
install %{SOURCE21} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/server.key
%endif

CFG="$RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf/"

install %{SOURCE6} $CFG/10_httpd.conf
install %{SOURCE8} $CFG/20_mod_vhost_alias.conf
install %{SOURCE9} $CFG/25_mod_status.conf
install %{SOURCE10} $CFG/30_mod_proxy.conf
install %{SOURCE11} $CFG/35_mod_info.conf
install %{SOURCE12} $CFG/40_mod_ssl.conf
install %{SOURCE13} $CFG/45_mod_dav.conf
install %{SOURCE14} $CFG/59_mod_dir.conf
install %{SOURCE15} $CFG/13_mod_suexec.conf
install %{SOURCE16} $CFG/58_mod_deflate.conf
install %{SOURCE17} $CFG/57_mod_autoindex.conf

echo "LoadModule ldap_module	%{_libexecdir}/mod_ldap.so" > $CFG/49_mod_ldap.conf
echo "LoadModule actions_module	%{_libexecdir}/mod_actions.so" > $CFG/50_mod_actions.conf
echo "LoadModule auth_module	%{_libexecdir}/mod_auth.so" > $CFG/51_mod_auth.conf
#echo "LoadModule auth_anon_module	%{_libexecdir}/mod_auth_anon.so" > $CFG/52_mod_auth_anon.conf
#echo "LoadModule auth_dbm_module	%{_libexecdir}/mod_auth_dbm.so" > $CFG/53_mod_auth_dbm.conf
echo "LoadModule auth_digest_module	%{_libexecdir}/mod_auth_digest.so" > $CFG/54_mod_auth_digest.conf
echo "LoadModule cache_module	%{_libexecdir}/mod_cache.so
LoadModule mem_cache_module	%{_libexecdir}/mod_mem_cache.so
LoadModule disk_cache_module	%{_libexecdir}/mod_disk_cache.so" > $CFG/55_mod_cache.conf
echo "LoadModule cgid_module	%{_libexecdir}/mod_cgid.so" > $CFG/56_mod_cgid.conf
echo "LoadModule charset_lite_module	%{_libexecdir}/mod_charset_lite.so" > $CFG/57_mod_charset_lite.conf
echo "LoadModule auth_ldap_module	%{_libexecdir}/mod_auth_ldap.so" > $CFG/59_mod_auth_ldap.conf
echo "LoadModule expires_module	%{_libexecdir}/mod_expires.so" > $CFG/60_mod_expires.conf
echo "LoadModule file_cache_module	%{_libexecdir}/mod_file_cache.so" > $CFG/61_mod_file_cache.conf
echo "LoadModule headers_module	%{_libexecdir}/mod_headers.so" > $CFG/62_mod_headers.conf
echo "LoadModule imap_module	%{_libexecdir}/mod_imap.so" > $CFG/63_mod_imap.conf
echo "LoadModule rewrite_module	%{_libexecdir}/mod_rewrite.so" > $CFG/64_mod_rewrite.conf
echo "LoadModule usertrack_module	%{_libexecdir}/mod_usertrack.so" > $CFG/65_mod_usertrack.conf
echo "LoadModule unique_id_module	%{_libexecdir}/mod_unique_id.so" > $CFG/66_mod_unique_id.conf

ln -sf index.html.en $RPM_BUILD_ROOT%{_datadir}/html/index.html
# let's remove trash (yes, *.html without lang suffix also contain trash)
find $RPM_BUILD_ROOT%{_datadir}/manual -type f \
	-name '*.xml' -o -name '*.xml.*' -o -name '*.html' \
	| xargs rm -f

# drop more
rm -rf $RPM_BUILD_ROOT%{_datadir}/manual/style

# find manual files
:> manual.files
cur=$(pwd)
echo "%{_datadir}/manual/LICENSE" >> "$cur/manual.files"
cd $RPM_BUILD_ROOT
find ./%{_datadir}/manual -type d -printf "%%%%dir %{_datadir}/manual/%%P\n" >> "$cur/manual.files"
find ./%{_datadir}/manual -type f -printf "%{_datadir}/manual/%%P\n" | awk '
/\.(en|map|gif|png|jpg|ico)$/ { print $0; }
/\.de$/ { print "%%lang(de) ", $0; }
/\.es$/ { print "%%lang(es) ", $0; }
/\.fr$/ { print "%%lang(fr) ", $0; }
/\.ja\..*$/ { print "%%lang(ja) ", $0; }
/\.ko\..*$/ { print "%%lang(ko) ", $0; }
/\.pt-br$/ { print "%%lang(pt_BR) ", $0; }
/\.ru\..*$/ { print "%%lang(ru) ", $0; }
' >> "$cur/manual.files"
cd $cur

# htpasswd goes to %{_bindir}
mv $RPM_BUILD_ROOT%{_sbindir}/htpasswd $RPM_BUILD_ROOT%{_bindir}/
ln -sf %{_bindir}/htpasswd $RPM_BUILD_ROOT%{_sbindir}/

# cgi_test: create config file with ScriptAlias
cat << EOF > $CFG/09_cgi_test.conf
ScriptAlias /cgi-bin/printenv %{_cgibindir}/printenv
ScriptAlias /cgi-bin/test-cgi %{_cgibindir}/test-cgi
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 51 http
%useradd -u 51 -r -d /home/services/httpd -s /bin/false -c "HTTP User" -g http http

%post
/sbin/chkconfig --add httpd
umask 137
touch /var/log/httpd/{access,error,agent,referer}_log

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd stop 1>&2
	fi
	# see http://thread.gmane.org/gmane.linux.pld.devel.english/712
	[ ! -x /sbin/chkconfig ] || /sbin/chkconfig --del httpd
fi

%postun
if [ "$1" = "0" ]; then
	%userremove http
	%groupremove http
fi

%triggerpostun -- %{name} <= 2.0.50-6
%banner %{name}-2.0.50-6 << EOF
WARNING!!!
Since apache-2.0.50-6 autoindex module has been separated to package
%{name}-mod_autoindex If you want to have the same functionality do:
poldek -Uv %{name}-mod_autoindex
EOF

%triggerpostun -- %{name} < 2.0.54-4
%banner %{name}-2.0.54-2 << EOF
WARNING!!!
CGI demo/test programs - printenv and test-cgi, have been released
from package apache into separate subpackage apache-cgi_test. If you
need printenv and/or test-cgi, please install apache-cgi_test package,
e.g. by running poldek -Uv apache-cgi_test
EOF

# update /etc/sysconfig/apache -> httpd rename
if [ -f /etc/sysconfig/apache.rpmsave ]; then
	cp -f /etc/sysconfig/httpd{,.rpmnew}
	mv -f /etc/sysconfig/{apache.rpmsave,httpd}
fi

%triggerpostun -- %{name} < 2.0.55-3.1
if ! grep -q 'Include webapps.d/' /etc/httpd/httpd.conf/10_httpd.conf; then
# make sure webapps.d is included
cp -f /etc/httpd/httpd.conf/10_httpd.conf{,.rpmsave}
# this file is ugly, so just append new lines
cat <<EOF >> /etc/httpd/httpd.conf/10_httpd.conf
# Include webapps config
Include webapps.d/*.conf
EOF
fi

# rename monitrc to be service name like other files
if [ -f /etc/monit/apache.monitrc.rpmsave ]; then
	mv -f /etc/monit/httpd.monitrc{,.rpmnew}
	mv -f /etc/monit/{apache.monitrc.rpmsave,httpd.monitrc}
fi

%posttrans
# minimizing apache restarts logics. we restart webserver:
#
# 1. at the end of transaction. (posttrans, feature from rpm 4.4.2)
# 2. first install of module (post: $1 = 1)
# 2. uninstall of module (postun: $1 == 0)
#
# the strict internal deps between apache modules and
# main package are very important for all this to work.

# restart webserver at the end of transaction
%service httpd restart

# macro called at module post scriptlet
%define	module_post \
if [ "$1" = "1" ]; then \
	%service -q httpd restart \
fi

# macro called at module postun scriptlet
%define	module_postun \
if [ "$1" = "0" ]; then \
	%service -q httpd restart \
fi

%post mod_actions
%module_post

%postun mod_actions
%module_postun

#%post mod_auth
#%module_post
#
#%postun mod_auth
#%module_postun

#%post mod_auth_anon
#%module_post
#
#%postun mod_auth_anon
#%module_postun

#%post mod_auth_dbm
#%module_post
#
#%postun mod_auth_dbm
#%module_postun

%post mod_autoindex
%module_post

%postun mod_autoindex
%module_postun

%post mod_cache
%module_post

%postun mod_cache
%module_postun

%post mod_cgid
%module_post

%postun mod_cgid
%module_postun

%post mod_charset_lite
%module_post

%postun mod_charset_lite
%module_postun

%post mod_dav
%module_post

%postun mod_dav
%module_postun

#%post mod_auth_digest
#%module_post
#
#%postun mod_auth_digest
#%module_postun

%post mod_deflate
%module_post

%postun mod_deflate
%module_postun

%post mod_dir
%module_post

%postun mod_dir
%module_postun

%post mod_expires
%module_post

%postun mod_expires
%module_postun

%post mod_file_cache
%module_post

%postun mod_file_cache
%module_postun

%post mod_headers
%module_post

%postun mod_headers
%module_postun

%post mod_imap
%module_post

%postun mod_imap
%module_postun

%post mod_info
%module_post

%postun mod_info
%module_postun

%post mod_proxy
%module_post

%postun mod_proxy
%module_postun

%post mod_rewrite
%module_post

%postun mod_rewrite
%module_postun

%post mod_ssl
%module_post

%postun mod_ssl
%module_postun

%post mod_status
%module_post

%postun mod_status
%module_postun

%post mod_usertrack
%module_post

%postun mod_usertrack
%module_postun

%post mod_unique_id
%module_post

%postun mod_unique_id
%module_postun

%post mod_vhost_alias
%module_post

%postun mod_vhost_alias
%module_postun

%post cgi_test
if [ "$1" = "1" ]; then
	%service -q httpd reload
fi

%postun cgi_test
if [ "$1" = "0" ]; then
	%service -q httpd reload
fi

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE CHANGES README
%doc docs/conf/mime.types

%attr(754,root,root) /etc/rc.d/init.d/httpd

# TODO: switch to conf.d, instead of confusing *dir* httpd.conf
%attr(750,root,root) %dir %{_sysconfdir}/httpd.conf
%attr(750,root,root) %dir %{_sysconfdir}/webapps.d
%attr(750,root,root) %dir %{_sysconfdir}/modules
%attr(750,root,root) %dir %{_sysconfdir}/run
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_httpd.conf
%attr(640,root,root) %{_sysconfdir}/magic
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/httpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/monit/*.monitrc

#%attr(755,root,root) %{_libexecdir}/mod_access.so
%attr(755,root,root) %{_libexecdir}/mod_alias.so
%attr(755,root,root) %{_libexecdir}/mod_asis.so
%attr(755,root,root) %{_libexecdir}/mod_cern_meta.so
%attr(755,root,root) %{_libexecdir}/mod_cgi.so
%attr(755,root,root) %{_libexecdir}/mod_env.so
%attr(755,root,root) %{_libexecdir}/mod_include.so
%attr(755,root,root) %{_libexecdir}/mod_log_config.so
%attr(755,root,root) %{_libexecdir}/mod_log_forensic.so
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
%attr(755,root,root) %{_sbindir}/checkgid
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/httpd.*
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs

%dir %attr(770,root,http) /var/run/apache
%dir %attr(770,root,http) /var/cache/apache

%{_mandir}/man1/htdigest.1*
%{_mandir}/man8/ab.8*
%{_mandir}/man8/apachectl.8*
%{_mandir}/man8/httpd.8*
%{_mandir}/man8/logresolve.8*
%{_mandir}/man8/rotatelogs.8*

%attr(2750,root,logs) %dir /var/log/httpd
%attr(2750,root,logs) %dir /var/log/archiv/httpd
%attr(640,root,logs) %ghost /var/log/httpd/*

%dir %{_datadir}

%dir %{_datadir}/cgi-bin
%dir %{_datadir}/html
%{_datadir}/icons
%{_datadir}/error

%files doc -f manual.files
%defattr(644,root,root,755)

%files suexec
%defattr(644,root,root,755)
%attr(4755,root,root) %{_sbindir}/suexec
%attr(755,root,root) %{_libexecdir}/mod_suexec.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_suexec.conf
%{_mandir}/man8/suexec.8*

%files index
%defattr(644,root,root,755)
%config(noreplace,missingok) %{_datadir}/html/index.html*
%{_datadir}/html/*.gif
%{_datadir}/html/*.png

%files apxs
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/envvars*
%attr(751,root,root) %dir %{_sysconfdir}
%dir %{_libexecdir}
%dir %{_libexecdir}/build
%{_libexecdir}/build/config_vars.mk
%{_mandir}/man8/apxs.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}
%{_libexecdir}/*.exp
%attr(750,root,root) %dir %{_sysconfdir}/build
%{_libexecdir}/build/[lprs]*.mk
%attr(755,root,root) %{_libexecdir}/build/*.sh
%attr(755,root,root) %{_libexecdir}/build/libtool

%files mod_actions
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_actions.conf
%attr(755,root,root) %{_libexecdir}/mod_actions.so

%files mod_auth
%defattr(644,root,root,755)

#%files mod_auth_anon
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth_anon.conf
#%attr(755,root,root) %{_libexecdir}/mod_auth_anon.so

%files mod_auth_basic
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_basic.so

%files mod_auth_dbm
%defattr(644,root,root,755)

%files mod_auth_digest
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth_digest.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_digest.so

#%if %{with ldap}
#%files mod_auth_ldap
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth_ldap.conf
#%attr(755,root,root) %{_libexecdir}/mod_auth_ldap.so
#%endif

%files mod_authn_alias
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_alias.so

%files mod_authn_anon
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_anon.so

%files mod_authn_dbd
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_dbd.so

%files mod_authn_dbm
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_dbm.so

%files mod_authn_default
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_default.so

%files mod_authn_file
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_file.so

%if %{with ldap}
%files mod_authnz_ldap
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authnz_ldap.so
%endif

%files mod_authz_dbm
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_dbm.so

%files mod_authz_default
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_default.so

%files mod_authz_groupfile
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_groupfile.so

%files mod_authz_host
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_host.so

%files mod_authz_owner
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_owner.so

%files mod_authz_user
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_user.so

%files mod_autoindex
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_autoindex.conf
%attr(755,root,root) %{_libexecdir}/mod_autoindex.so

%if %{with bucketeer}
%files mod_bucketeer
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_bucketeer.so
%endif

%files mod_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_cache.conf
%attr(755,root,root) %{_sbindir}/htcacheclean
%attr(755,root,root) %{_libexecdir}/mod_cache.so
%attr(755,root,root) %{_libexecdir}/mod_disk_cache.so
%attr(755,root,root) %{_libexecdir}/mod_mem_cache.so
%{_mandir}/man8/htcacheclean.8*

%files mod_cgid
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_cgid.conf
%attr(755,root,root) %{_libexecdir}/mod_cgid.so

%files mod_charset_lite
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_charset_lite.conf
%attr(755,root,root) %{_libexecdir}/mod_charset_lite.so

%files mod_dav
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_dav.conf
%attr(755,root,root) %{_libexecdir}/mod_dav*.so
%dir %attr(770,root,http) /var/lock/mod_dav

%files mod_dbd
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_dbd.so

%files mod_deflate
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_deflate.conf
%attr(755,root,root) %{_libexecdir}/mod_deflate.so

%files mod_dir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_dir.conf
%attr(755,root,root) %{_libexecdir}/mod_dir.so

%files mod_dumpio
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_dumpio.so

%files mod_expires
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_expires.conf
%attr(755,root,root) %{_libexecdir}/mod_expires.so

%files mod_file_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_file_cache.conf
%attr(755,root,root) %{_libexecdir}/mod_file_cache.so

%files mod_filter
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_filter.so

%files mod_headers
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_headers.conf
%attr(755,root,root) %{_libexecdir}/mod_headers.so

%files mod_ident
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_ident.so

%files mod_imagemap
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_imagemap.so

#%files mod_imap
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_imap.conf
#%attr(755,root,root) %{_libexecdir}/mod_imap.so

%files mod_info
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_info.conf
%attr(755,root,root) %{_libexecdir}/mod_info.so

%if %{with ldap}
%files mod_ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_ldap.so
%endif

%files mod_logio
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_logio.so

%files mod_proxy
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_proxy.conf
%attr(755,root,root) %{_libexecdir}/mod_proxy*.so

%files mod_rewrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/httxt2dbm
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_rewrite.conf

%if %{with ssl}
%files mod_ssl
%defattr(644,root,root,755)
%attr(750,root,root) %dir %{_sysconfdir}/ssl
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ssl/server.*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_ssl.conf
%attr(755,root,root) %{_libexecdir}/mod_ssl.so
%endif

%files mod_status
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_status.conf
%attr(755,root,root) %{_libexecdir}/mod_status.so

%files mod_unique_id
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_unique_id.conf
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so

%files mod_usertrack
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_usertrack.conf
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so

%files mod_version
%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_auth.conf
%attr(755,root,root) %{_libexecdir}/mod_version.so

%files mod_vhost_alias
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_vhost_alias.conf

%files -n htpasswd-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htpasswd
%attr(755,root,root) %{_sbindir}/htpasswd
%{_mandir}/man1/htpasswd.1*

%files dbmtools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/dbmmanage
%attr(755,root,root) %{_sbindir}/htdbm
%{_mandir}/man1/dbmmanage.1*
%{_mandir}/man1/htdbm.1*

%files cgi_test
%defattr(644,root,root,755)
%dir %{_cgibindir}
%attr(755,root,root) %{_cgibindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/09_cgi_test.conf

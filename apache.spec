# TODO:
# - config examples for mod_*
# - --with-suexec-uidmin=500 or =1000 ?
# - subpackages for MPMs
# - !!!check if all modules (*.so) are exactly the same for different MPMs
# - check those autn modules inner deps
# - for external packages: don't use any apache module name in dep as they
#   differ for apache 1.3/2.0/2.2!? any better ideas? rpm Suggests: tags?
# - for mod_auth_* modules require each auth module to require virtual authn so at least *_default is chosen?
# - same for mod_authz
# - mod_auth_digest and mod_auth_basic R: apache(authn) ?
# - drop mod_case_filter* or find summary and description for them
# - build modules only once (not with each mpm)

# Conditional build:
%bcond_without	ssl		# build without SSL support
%bcond_without	ldap		# build without LDAP support
%bcond_without	metuxmpm	# metux MPM
%bcond_without	peruser		# peruser MPM
%bcond_without	event		# event MPM
%bcond_with	distcache	# distcache support
%bcond_with	bucketeer	# debug one
#
%include	/usr/lib/rpm/macros.perl
# this is internal macro, don't change to %%apache_modules_api
%define		_apache_modules_api 20051115
Summary:	The most widely used Web server on the Internet
Summary(de.UTF-8):	Leading World Wide Web-Server
Summary(es.UTF-8):	Servidor HTTPD para proveer servicios WWW
Summary(fr.UTF-8):	Le serveur web le plus utilise sur Internet
Summary(pl.UTF-8):	Serwer WWW (World Wide Web)
Summary(pt_BR.UTF-8):	Servidor HTTPD para prover serviços WWW
Summary(ru.UTF-8):	Самый популярный веб-сервер
Summary(tr.UTF-8):	Lider WWW tarayıcı
Name:		apache
Version:	2.2.11
Release:	2
License:	Apache v2.0
Group:		Networking/Daemons/HTTP
Source0:	http://www.apache.org/dist/httpd/httpd-%{version}.tar.gz
# Source0-md5:	03e0a99a5de0f3f568a0087fb9993af9
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	%{name}.sysconfig
Source4:	%{name}-server.crt
Source5:	%{name}-server.key
Source6:	%{name}-httpd.conf
Source7:	%{name}-common.conf
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
Source18:	%{name}-multilang-errordoc.conf
Source19:	%{name}-manual.conf
Source20:	%{name}-mod_userdir.conf
Source21:	%{name}-mpm.conf
Source22:	%{name}-languages.conf
Source23:	%{name}-mod_mime.conf
Source24:	%{name}-mod_authz_host.conf
Source25:	%{name}-mod_cgid.conf
Source26:	%{name}-mod_log_config.conf
Source27:	%{name}-mod_mime_magic.conf
Source28:	%{name}-mod_cache.conf
Patch0:		%{name}-configdir_skip_backups.patch
Patch1:		%{name}-layout.patch
Patch2:		%{name}-suexec.patch
Patch3:		%{name}-branding.patch
Patch4:		%{name}-apr.patch
# project homepage http://www.metux.de/mpm/en/?patpage=index
# http://www.sannes.org/metuxmpm/
Patch5:		httpd-2.0.48-metuxmpm-r8.patch
# what about this? it isn't applied...
Patch6:		httpd-2.0.40-xfsz.patch
Patch7:		%{name}-syslibs.patch
Patch8:		httpd-2.0.45-encode.patch
Patch9:		%{name}-paths.patch
Patch10:	httpd-2.0.46-dav401dest.patch
Patch11:	%{name}-bug-40970.patch
Patch12:	httpd-2.0.46-sslmutex.patch
Patch14:	httpd-2.0.48-corelimit.patch
Patch15:	httpd-2.0.48-debuglog.patch
Patch18:	%{name}-v6only-ENOPROTOOPT.patch
Patch19:	%{name}-conffile-path.patch
Patch20:	%{name}-apxs.patch
# http://www.telana.com/peruser.php (2.2.3-0.3.0)
Patch21:	httpd-peruser.patch
Patch23:	%{name}-suexec_fcgi.patch
Patch24:	%{name}-revert-bug-40463.patch
URL:		http://httpd.apache.org/
BuildRequires:	apr-devel >= 1:1.2
BuildRequires:	apr-util-devel >= 1:1.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
%{?with_distcache:BuildRequires:	distcache-devel}
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	libtool >= 2:1.5
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_ssl:BuildRequires:	openssl-tools >= 0.9.7d}
BuildRequires:	pcre-devel
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
# packages that were in apache-2.0.rpm, for compatibility
Requires:	%{name}-errordocs = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_asis = %{version}-%{release}
Requires:	%{name}-mod_auth = %{version}-%{release}
Requires:	%{name}-mod_cern_meta = %{version}-%{release}
Requires:	%{name}-mod_cgi = %{version}-%{release}
Requires:	%{name}-mod_env = %{version}-%{release}
Requires:	%{name}-mod_include = %{version}-%{release}
Requires:	%{name}-mod_log_config = %{version}-%{release}
Requires:	%{name}-mod_mime = %{version}-%{release}
Requires:	%{name}-mod_mime_magic = %{version}-%{release}
Requires:	%{name}-mod_negotiation = %{version}-%{release}
Requires:	%{name}-mod_setenvif = %{version}-%{release}
Requires:	%{name}-mod_speling = %{version}-%{release}
Requires:	%{name}-mod_userdir = %{version}-%{release}
Requires:	%{name}-mod_version = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}
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

%description -l de.UTF-8
Apache ist ein voll funktionsfähiger Web-Server, der kostenlos
erhältlich und weit verbreitet ist.

%description -l es.UTF-8
El servidor web Apache es el mejor servidor gratuito disponible en el
mundo UNIX hoy. Usa HTTP (HyperText Transfer Protocol) para permitir
que navegadores vean documentos y sometan datos remotamente. Puede
ejecutar varias funciones diferentes, incluyendo funciones de proxy y
caché, y nos ofrece características como monitor de estado, conversión
dinámica de tipo, y otras más.

%description -l fr.UTF-8
Apache est un serveur Web puissant, efficace, gratuit et complet.
Apache est aussi le serveur Web le plus populaire sur Internet.

%description -l pl.UTF-8
Apache jest serwerem WWW (World Wide Web). Instalując ten pakiet
będziesz mógł prezentować własne strony WWW w sieci Internet.

%description -l pt_BR.UTF-8
O servidor web Apache é o melhor servidor gratuito disponível no mundo
UNIX hoje. Ele usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vejam documentos e submetam dados remotamente. Ele
pode executar várias funções diferentes, incluindo funções de proxy e
cache, e oferece características como monitor de status, conversão
dinâmica de tipo, e mais.

%description -l ru.UTF-8
Apache - мощный, функциональный, высокопроизводительный и свободно
распространяемый веб-сервер.

%description -l tr.UTF-8
Apache serbest dağıtılan ve çok kullanılan yetenekli bir web
sunucusudur.

%package base
Summary:	The Number One HTTP Server On The Internet
Summary(pl.UTF-8):	Wiodący w Internecie serwer HTTP
Group:		Networking/Daemons/HTTP
Requires(post):	fileutils
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	/sbin/chkconfig
Requires:	apr >= 1:1.2
Requires:	psmisc >= 20.1
Requires:	rc-scripts >= 0.4.0.15
Requires:	webapps
Provides:	apache(modules-api) = %{_apache_modules_api}
Provides:	group(http)
Provides:	user(http)
Provides:	webserver = apache
Obsoletes:	apache-extra
Obsoletes:	apache6
# packaged by mistake. really sample code
Obsoletes:	apache-mod_optional_fn_export
Obsoletes:	apache-mod_optional_fn_import
Obsoletes:	apache-mod_optional_fn_import
Obsoletes:	apache-mod_optional_hook_import
Conflicts:	apache < 2.2.0
Conflicts:	logrotate < 3.7-4
# for the posttrans scriptlet, conflicts because in vserver environment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2

%description base
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%description base -l pl.UTF-8
Apache jest potężnym, w pełni funkcjonalnym, wydajnym i wolnodostępnym
serwerem WWW (World Wide Web). Jest także najbardziej popularnym
serwerem WWW w Internecie.

%package suexec
Summary:	Apache suexec wrapper
Summary(pl.UTF-8):	Wrapper suexec do serwera WWW Apache
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/suexec.html
Requires:	%{name}-base = %{version}-%{release}

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and
SSI programs under user IDs different from the user ID of the calling
web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description suexec -l pl.UTF-8
SuEXEC umożliwia serwerowi Apache uruchamianie programów CGI i SSI z
innym UID niż wywołujący je serwer. Normalnie programy CGI i SSI są
wykonywane jako taki sam użytkownik jak serwer WWW.

%package tools
Summary:	Apache tools
Summary(pl.UTF-8):	Narzędzia Apache'a
Group:		Development/Tools

%description tools
Apache tools.

%description tools -l pl.UTF-8
Narzędzia Apache'a.

%package index
Summary:	Apache index.html* files
Summary(pl.UTF-8):	Pliki Apache index.html*
Group:		Documentation
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	indexhtml

%description index
Apache index.html* files.

%description index -l pl.UTF-8
Pliki index.html* Apache'a.

%package doc
Summary:	Apache manual
Summary(pl.UTF-8):	Podręcznik Apache'a
Group:		Documentation
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_dir = %{version}-%{release}
Requires:	%{name}-mod_negotiation = %{version}-%{release}
Requires:	%{name}-mod_setenvif = %{version}-%{release}

%description doc
Apache manual.

%description doc -l pl.UTF-8
Podręcznik Apache'a.

%package errordocs
Summary:	Multi-language error messages for Apache
Summary(pl.UTF-8):	Wielojęzyczne komunikaty błędów dla Apache'a
Group:		Applications/WWW
URL:		http://httpd.apache.org/docs-project/
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Requires:	%{name}-mod_include = %{version}-%{release}
Requires:	%{name}-mod_negotiation = %{version}-%{release}

%description errordocs
Multi-language error messages.

%description errordocs -l pl.UTF-8
Dokumenty opisujące błędy HTTP dla Apache'a w wielu językach.

%package devel
Summary:	Module development tools for the Apache web server
Summary(es.UTF-8):	Archivos de inclusión del Apache para desarrollo de módulos
Summary(fr.UTF-8):	Les outils de developpement de modules pour le serveur web Apache
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia modułów rozszerzeń do serwera WWW Apache
Summary(pt_BR.UTF-8):	Arquivos de inclusão do Apache para desenvolvimento de módulos
Summary(ru.UTF-8):	Средства разработки модулей для веб-сервера Apache
Group:		Networking/Utilities
Requires:	apr-util-devel >= 1:1.2
Requires:	libtool
Obsoletes:	apache-apxs
Obsoletes:	apache-static

%description devel
The apache-devel package contains header files for Apache.

%description devel -l es.UTF-8
Este paquete contiene los archivos de inclusión para el Apache, bien
como el utilitario apxs para la construcción de objetos compartidos
dinámicos (DSOs). Ha ce falta instalar este paquete si deseas compilar
o desarrollar módulos adicionales para Apache.

%description devel -l fr.UTF-8
Le package apache-devel contient le code source pour le serveur Web
Apache et le binaire APXS dont vous aurez besoin pour construire des
Objets Dynamiques Partages (DSOs) pour Apache.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne zasoby niezbędne przy budowaniu modułów DSO
(Dynamic Shared Objects) dla Apache'a.

%description devel -l ru.UTF-8
Средства разработки модулей для веб-сервера Apache.

%description devel -l pt_BR.UTF-8
Este pacote contem os arquivos de inclusão para o Apache, bem como o
utilitário apxs para a construção de objetos compartilhados dinâmicos
(DSOs). Este pacote precisa ser instalado se você deseja compilar ou
desenvolver módulos adicionais para o Apache.

%package mod_actions
Summary:	Apache module for executing CGI scripts based on media type or request method
Summary(pl.UTF-8):	Moduł Apache'a do uruchamiania skryptów CGI w oparciu o rodzaj danych lub żądania
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_actions.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_actions) = %{version}-%{release}

%description mod_actions
This module has two directives. The Action directive lets you run CGI
scripts whenever a file of a certain MIME content type is requested.
The Script directive lets you run CGI scripts whenever a particular
method is used in a request. This makes it much easier to execute
scripts that process files.

%description mod_actions -l pl.UTF-8
Ten moduł ma dwie dyrektywy. Dyrektywa Action pozwala uruchamiać
skrypty CGI przy żądaniu pliku o danym typie zawartości MIME.
Dyrektywa Script pozwala uruchamiać skrypty CGI przy danej metodzie
żądania. Znacznie ułatwia to wykonywanie skryptów przetwarzających
pliki.

%package mod_alias
Summary:	Mapping different parts of the host filesystem in the document tree and for URL redirection
Summary(pl.UTF-8):	Odwzorowywanie różnych części systemu plików w drzewie dokumentów i przekierowywanie URL-i
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_alias.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_alias) = %{version}-%{release}
Provides:	webserver(alias)

%description mod_alias
The directives contained in this module allow for manipulation and
control of URLs as requests arrive at the server. The Alias and
ScriptAlias directives are used to map between URLs and filesystem
paths. This allows for content which is not directly under the
DocumentRoot served as part of the web document tree. The ScriptAlias
directive has the additional effect of marking the target directory as
containing only CGI scripts.

The Redirect directives are used to instruct clients to make a new
request with a different URL. They are often used when a resource has
moved to a new location.

mod_alias is designed to handle simple URL manipulation tasks. For
more complicated tasks such as manipulating the query string, use the
tools provided by mod_rewrite.

%description mod_alias -l pl.UTF-8
Dyrektywy zawarte w tym module umożliwiają manipulacje i sterowanie
URL-ami kiedy żądania są dostarczane do serwera. Dyrektywy Alias i
ScriptAlias są używane do odwzorowywania między URL-ami i ścieżkami w
systemie plików. Umożliwia to serwowanie treści nie będącej
bezpośrednio wewnątrz DocumentRoota jako część drzewa dokumentów WWW.
Dyrektywa ScriptAlias ma dodatkowy efekt oznaczania katalogu
docelowego jako zawierającego wyłącznie skrypty CGI.

Dyrektywy Redirect służą do instruowania klientów, aby wykonali nowe
żądanie z innym URL-em. Są używane zwykle w przypadku, gdy zasoby
zostały przeniesione w inne miejsce.

mod_alias został zaprojektowany do obsługi prostych manipulacji na
URL-ach. Bardziej skomplikowane zadania, takie jak modyfikowanie
łańcucha zapytania można wykonać przy użyciu mod_rewrite.

%package mod_asis
Summary:	Sends files that contain their own HTTP headers
Summary(pl.UTF-8):	Wysyłanie plików zawierających własne nagłówki HTTP
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_asis.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_asis) = %{version}-%{release}

%description mod_asis
This module provides the handler send-as-is which causes Apache to
send the document without adding most of the usual HTTP headers.

This can be used to send any kind of data from the server, including
redirects and other special HTTP responses, without requiring a
cgi-script or an nph script.

For historical reasons, this module will also process any file with
the mime type httpd/send-as-is.

%description mod_asis -l pl.UTF-8
Ten moduł udostępnia procesurę obsługi send-as-is powodującą, że
Apache wysyła dokument bez dodawania większości zwykle używanych
nagłówków HTTP.

Może to być używane do wysyłania dowolnego rodzaju danych z serwera,
włącznie z przekierowaniami i innymi specjalnymi odpowiedziami HTTP
bez wymagania skryptu CGI lub nph.

%package mod_auth
Summary:	Virtual package which provides backward compatibility with apache 2.0
Summary(pl.UTF-8):	Pakiet wirtualny zapewniający kompatybilność wsteczną z apache 2.0
Group:		Networking/Daemons/HTTP
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_auth_basic = %{version}-%{release}
Requires:	%{name}-mod_authn_file = %{version}-%{release}
Requires:	%{name}-mod_authz_groupfile = %{version}-%{release}
Requires:	%{name}-mod_authz_user = %{version}-%{release}
Provides:	apache(mod_auth) = %{version}-%{release}
Provides:	webserver(auth)

%description mod_auth
Virtual package which requires apache-mod_authn_file,
apache-mod_authz_user and apache-mod_authz_groupfile for backward
compatibility with apache 2.0.

%description mod_auth -l pl.UTF-8
Pakiet wirtualny wymagający apache-mod_authn_file,
apache-mod_authz_user i apache-mod_authz_groupfile dla kompatybilności
wstecznej z apache 2.0.

%package mod_auth_basic
Summary:	Apache module that allows Basic authentication
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający korzystawnie z uwierzytelnienia Basic
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_auth_basic.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_auth_basic) = %{version}-%{release}

%description mod_auth_basic
This module allows the use of HTTP Basic Authentication to restrict
access by looking up users in the given providers.

HTTP Digest Authentication is provided by mod_auth_digest. This module
should usually be combined with at least one authentication module
such as mod_authn_file and one authorization module such as
mod_authz_user.

%description mod_auth_basic -l pl.UTF-8
Ten moduł pozwala używać uwierzytelnienia HTTP Basic do ograniczania
dostępu poprzez wyszukiwanie użytkowników we wskazanych miejscach

%package mod_auth_dbm
Summary:	Virtual package which provides backward compatibility with apache 2.0
Summary(pl.UTF-8):	Pakiet wirtualny zapewniający kompatybilność wsteczną z apache 2.0
Group:		Networking/Daemons/HTTP
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-dbmtools = %{version}-%{release}
Requires:	%{name}-mod_authn_dbm = %{version}-%{release}
Requires:	%{name}-mod_authz_dbm = %{version}-%{release}
Provides:	apache(mod_auth_dbm) = %{version}-%{release}

%description mod_auth_dbm
Virtual package which requires apache-mod_authn_dbm and
apache-mod_authz_dbm for backward compatibility with apache 2.0.

%description mod_auth_dbm -l pl.UTF-8
Pakiet wirtualny wymagający apache-mod_authn_dbm i
apache-mod_authz_dbm dla kompatybilności wstecznej z apache 2.0.

%package mod_auth_digest
Summary:	User authentication using MD5 Digest Authentication
Summary(pl.UTF-8):	Uwierzytelnianie użytkowników przy użyciu MD5 Digest
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_auth_digest.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_auth_digest) = %{version}-%{release}

%description mod_auth_digest
This module implements HTTP Digest Authentication. However, it has not
been extensively tested and is therefore marked experimental.

%description mod_auth_digest -l pl.UTF-8
Ten moduł implementuje uwierzytelnienie HTTP Digest. Nie został on
jednak zbyt obszernie przetestowany, więc jest oznaczony jako
eksperymentalny.

%package mod_authn_alias
Summary:	Apache module that provides the ability to create extended authentication
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający tworzenie rozszerzonego uwierzytelniania
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_alias.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_alias) = %{version}-%{release}

%description mod_authn_alias
This module allows extended authentication providers to be created
within the configuration file and assigned an alias name.

%description mod_authn_alias -l pl.UTF-8
Ten moduł umożliwia tworzenie rozszerzonych sposobów uwierzytelniania
w pliku konfiguracyjnym i nadawanie im aliasów.

%package mod_authn_anon
Summary:	Apache module that allows "anonymous" user access to authenticated areas
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający dostęp anonimowych użytkowników do stref uwierzytelnianych
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_anon.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_anon) = %{version}-%{release}
# compat
Provides:	apache(mod_auth_anon) = %{version}-%{release}
Provides:	apache-mod_auth_anon = %{version}-%{release}
Obsoletes:	apache-mod_auth_anon < 2.2.0-0.5

%description mod_authn_anon
This module provides authentication front-ends such as mod_auth_basic
to authenticate users similar to anonymous-ftp sites, i.e. have a
'magic' user id 'anonymous' and the email address as a password. These
email addresses can be logged.

%description mod_authn_anon -l pl.UTF-8
Ten moduł udmożliwia frontendom uwierzytelniającym takim jak
mod_auth_basic uwierzytelnianie użytkowników podobnie do serwisów
anonimowego ftp, tzn. przez udostępnianie "magicznego" identyfikatora
"anonymous" i adresu pocztowego jako hasła. Te adresy pocztowe mogą
być logowane.

%package mod_authn_dbd
Summary:	Apache module that allows user authentication using an SQL
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający uwierzytelnianie użytkowników przy użyciu tabel SQL
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_dbd.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_dbd = %{version}-%{release}
Provides:	apache(mod_authn_dbd) = %{version}-%{release}

%description mod_authn_dbd
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in SQL
tables.

%description mod_authn_dbd -l pl.UTF-8
Ten moduł udostępnia frontendom uwierzytelniającym takim jak
mod_auth_digest i mod_auth_basic uwierzytelnianie użytkowników poprzez
wyszukiwanie w tabelach SQL.

%package mod_authn_dbm
Summary:	Apache module that allows user authentication using DBM files
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający uwierzytelnianie użytkowników przy użyciu plików DBM
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_dbm.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_dbm) = %{version}-%{release}

%description mod_authn_dbm
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in DBM
password files.

%description mod_authn_dbm -l pl.UTF-8
Ten moduł udostępnia frontendom uwierzytelniającym takim jak
mod_auth_digest i mod_auth_basic uwierzytelnianie użytkowników poprzez
wyszukiwanie w tabelach haseł DBM.

%package mod_authn_default
Summary:	Apache module that rejects any credentials supplied by the user
Summary(pl.UTF-8):	Moduł Apache'a odrzucający wszystkie dane podane przez użytkownika
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_default.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_default) = %{version}-%{release}

%description mod_authn_default
This module is designed to be the fallback module, if you don't have
configured an authentication module like mod_auth_basic. It simply
rejects any credentials supplied by the user.

%description mod_authn_default -l pl.UTF-8
Ten moduł został pomyślany jako domyślny moduł uwierzytelniający,
jeśli nie skonfigurowano modułu uwierzytelniającego takiego jak
mod_auth_basic. Moduł ten po prostu odrzuca wszelkie dane przekazane
przez użytkownika.

%package mod_authn_file
Summary:	Apache module that allows user authentication using text files
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający uwierzytelnianie użytkowników poprzez pliki tekstowe
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_file.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_file) = %{version}-%{release}

%description mod_authn_file
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in plain
text password files.

%description mod_authn_file -l pl.UTF-8
Ten moduł udostępnia frontendom uwierzytelniającym takim jak
mod_auth_digest i mod_auth_basic uwierzytelnianie użytkowników poprzez
wyszukiwanie w plikach tekstowych z hasłami.

%package mod_authnz_ldap
Summary:	Apache module that allows an LDAP directory to be used to store the database for HTTP Basic authentication
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający przechowywanie danych dla uwierzytelnienia HTTP Basic w bazie LDAP
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authnz_ldap.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_ldap = %{version}-%{release}
Requires:	apr-util-ldap
Provides:	apache(mod_authnz_ldap) = %{version}-%{release}
# compat
Provides:	apache(mod_auth_ldap) = %{version}-%{release}
Provides:	apache-mod_auth_ldap = %{version}-%{release}
Obsoletes:	apache-mod_auth_ldap < 2.2.0-0.5

%description mod_authnz_ldap
This module provides authentication front-ends such as mod_auth_basic
to authenticate users through an LDAP directory.

%description mod_authnz_ldap -l pl.UTF-8
Ten moduł udostępnia frontendom uwierzytelniającym takim jak
mod_auth_basic uwierzytelnianie użytkowników poprzez katalog LDAP.

%package mod_authz_dbm
Summary:	Apache module that allows group authorization using DBM files
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający uwierzytelnianie grup z użyciem plików DBM
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authz_dbm.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_dbm) = %{version}-%{release}

%description mod_authz_dbm
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by
group membership stored in DBM file.

%description mod_authz_dbm -l pl.UTF-8
Ten moduł daje możliwość udostępniania bądź blokowania części serwisu
WWW dla uwierzytelnionych użytkowników na podstawie ich przynależności
do grupy zapisywanej w pliku DBM.

%package mod_authz_default
Summary:	Apache module that rejects any authorization request
Summary(pl.UTF-8):	Moduł Apache'a odrzucający wszystkie żądania autoryzacji
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authz_default.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_default) = %{version}-%{release}

%description mod_authz_default
This module is designed to be the fallback module, if you don't have
configured an authorization module like mod_authz_user or
mod_authz_groupfile. It simply rejects any authorization request.

%description mod_authz_default -l pl.UTF-8
Ten moduł został pomyślany jako domyślny moduł autoryzujący jeśli nie
skonfigurowano modułu autoryzującego takiego jak mod_authz_user czy
mod_authz_groupfile. Moduł ten po prostu odrzuca wszelkie żądania
autoryzacji.

%package mod_authz_groupfile
Summary:	Apache module that allows group authorization using plaintext files
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający autoryzację grup przy użyciu plików tekstowych
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authz_groupfile.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_groupfile) = %{version}-%{release}

%description mod_authz_groupfile
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by
group membership stored in plain text file.

%description mod_authz_groupfile -l pl.UTF-8
Ten moduł daje możliwość udostępniania bądź blokowania części serwisu
WWW dla uwierzytelnionych użytkowników na podstawie ich przynależności
do grupy zapisywanej w pliku tekstowym.

%package mod_authz_host
Summary:	Apache module that allows group authorizations based on host (name or IP address)
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający autoryzację grup w oparcu o host (nazwę lub IP)
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_host) = %{version}-%{release}
# for apache < 2.2.0
Provides:	apache(mod_access) = %{version}-%{release}
Provides:	webserver(access)

%description mod_authz_host
The directives provided by mod_authz_host are used in <Directory>,
<Files>, and <Location> sections as well as .htaccess files to control
access to particular parts of the server. Access can be controlled
based on the client hostname, IP address, or other characteristics of
the client request, as captured in environment variables.

%description mod_authz_host -l pl.UTF-8
Dyrektyw udostępnianych przez mod_authz_host można używać w sekcjach
<Directory>, <Files> i <Location>, a także plikach .htaccess w celu
sterowania dostępem do poszczególnych części serwera. Dostępem można
sterować na podstawie nazwy hosta klienta, adresu IP lub innej
charakterystyki żądania klienta dostępnej w zmiennych środowiskowych.

%package mod_authz_owner
Summary:	Apache module that allows authorization based on file ownership
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający autoryzacje w oparciu o własność plików
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_authz_owner.html
Requires:	%{name}-base = %{version}-%{release}
#Requires:	any-auth-module
Provides:	apache(mod_authz_owner) = %{version}-%{release}

%description mod_authz_owner
This module authorizes access to files by comparing the userid used
for HTTP authentication (the web userid) with the file-system owner or
group of the requested file. The supplied username and password must
be already properly verified by an authentication module, such as
mod_auth_basic or mod_auth_digest.

%description mod_authz_owner -l pl.UTF-8
Ten moduł autoryzuje dostęp do plików poprzez porównanie
identyfikatora użytkownika użytego przy uwierzytelnianiu HTTP (web
userid) z właścicielem lub grupą żądanego pliku w systemie plików.
Podana nazwa użytkownika i hasło muszą być wcześniej zweryfikowane
przez moduł uwierzytelniania, taki jak mod_auth_basic lub
mod_auth_digest.

%package mod_authz_user
Summary:	Apache module that allows user authorization
Summary(pl.UTF-8):	Moduł Apache'a umożliwiający autoryzację użytkowników
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_authz_user.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_user) = %{version}-%{release}

%description mod_authz_user
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site.

%description mod_authz_user -l pl.UTF-8
Ten moduł daje możliwość udostępniania bądź blokowania części serwisu
WWW dla uwierzytelnionych użytkowników.

%package mod_autoindex
Summary:	Apache module - display index of files
Summary(pl.UTF-8):	Moduł apache do wyświetlania indeksu plików
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_autoindex.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Provides:	apache(mod_autoindex) = %{version}-%{release}

%description mod_autoindex
This package contains mod_autoindex module. It provides generation
index of files.

%description mod_autoindex -l pl.UTF-8
Ten pakiet dostarcza moduł autoindex, który generuje indeks plików.

%package mod_bucketeer
Summary:	buckets manipulation filter
Summary(pl.UTF-8):	Dzielenie kubełków po znalezieniu znaku sterującego
Group:		Networking/Daemons/HTTP
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_bucketeer) = %{version}-%{release}

%description mod_bucketeer
Split buckets whenever we find a control-char.

%description mod_bucketeer -l pl.UTF-8
Dzielenie kubełków po znalezieniu znaku sterującego.

%package mod_cache
Summary:	Content cache keyed to URIs
Summary(pl.UTF-8):	Pamięć podręczna wg klucza URI
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_cache.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_cache) = %{version}-%{release}

%description mod_cache
mod_cache implements an RFC 2616 compliant HTTP content cache that can
be used to cache either local or proxied content. Two storage
management modules are included in the base Apache distribution:
mod_disk_cache implements a disk based storage manager (generally used
for proxy caching) and mod_mem_cache implements an in-memory based
storage manager (primarily useful for caching local content).

%description mod_cache -l pl.UTF-8
Implementacja zgodnej z RFC 2616 pamięci podręcznej, która może być
używana do zapamiętywania zawartości lokalnej lub dostępnej przez
proxy. Dołączono dwa moduły pozwalające magazynować dane w pamięci
(głównie użyteczne przy cache'owaniu lokalnej zawartości) oraz na
dysku (używane do cache'owania proxy).

%package mod_case_filter
Summary:	TODO
Group:		Networking/Daemons/HTTP
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_case_filter) = %{version}-%{release}

%description mod_case_filter

%package mod_case_filter_in
Summary:	TODO
Group:		Networking/Daemons/HTTP
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_case_filter_in) = %{version}-%{release}

%description mod_case_filter_in

%package mod_cern_meta
Summary:	CERN httpd metafile semantics
Summary(pl.UTF-8):	Obsługa semantyki metaplików CERN httpd
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_cern_meta.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_cern_meta) = %{version}-%{release}

%description mod_cern_meta
Emulate the CERN HTTPD Meta file semantics. Meta files are HTTP
headers that can be output in addition to the normal range of headers
for each file accessed. They appear rather like the Apache .asis
files, and are able to provide a crude way of influencing the Expires:
header, as well as providing other curiosities. There are many ways to
manage meta information, this one was chosen because there is already
a large number of CERN users who can exploit this module.

%description mod_cern_meta -l pl.UTF-8
Moduł emulujący semantykę metaplików CERN HTTPD. Metapliki to nagłówki
HTTP, które mogą być wysyłane oprócz normalnego zestawu nagłówków dla
każdego przetwarzanego pliku. Zachowują się bardziej jak pliki .asis
Apache'a i mogą dawać brutalny sposób wpływania na nagłówek Expires:,
a także dostarczać inne ciekawostki. Jest wiele sposobów zarządzania
metainformacjami, ta została wybrana ponieważ istnieje już wielu
użytkowników CERN wykorzystujących ten moduł.

%package mod_cgi
Summary:	Execution of CGI scripts
Summary(pl.UTF-8):	Uruchamianie skryptów CGI
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_cgi.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Suggests:	%{name}-suexec = %{version}-%{release}
Provides:	apache(mod_cgi) = %{version}-%{release}
Provides:	webserver(cgi)

%description mod_cgi
Any file that has the mime type application/x-httpd-cgi or handler
cgi-script (Apache 1.1 or later) will be treated as a CGI script, and
run by the server, with its output being returned to the client. Files
acquire this type either by having a name containing an extension
defined by the AddType directive, or by being in a ScriptAlias
directory.

When using a multi-threaded MPM under unix, the module mod_cgid should
be used in place of this module. At the user level, the two modules
are essentially identical.

%description mod_cgi -l pl.UTF-8
Ten moduł powoduje, że dowolny plik o typie MIME
application/x-httpd-cgi albo procedurze obsługi cgi-script (w Apache'u
1.1 lub nowszym) będzie traktowany jako skrypt CGI i uruchamiany przez
serwer, a jego wyjście będzie zwracane klientowi. Pliki uzyskują ten
typ przez posiadanie nazwy zawierającej rozszerzenie określone
dyrektywą AddType lub będąc w katalogu ScriptAlias.

Przy używaniu wielowątkowych MPM pod uniksem zamiast tego modułu
należy używać modułu mod_cgid. Z poziomu użytkownika oba te moduły
zachowują się identycznie.

%package mod_cgid
Summary:	Execution of CGI scripts using an external CGI daemon
Summary(pl.UTF-8):	Uruchamianie zewnętrznych skryptów CGI za pomocą daemona CGI
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_cgid.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Provides:	apache(mod_cgid) = %{version}-%{release}
Provides:	webserver(cgi)

%description mod_cgid
Execution of CGI scripts using an external CGI daemon.

Except for the optimizations and the additional ScriptSock directive,
mod_cgid behaves similarly to mod_cgi.

This module should be used instead of mod_cgi whenever a
multi-threaded MPM is selected.

%description mod_cgid -l pl.UTF-8
Uruchamianie skryptów CGI za pomocą zewnętrznego demona CGI.

Z wyjątkiem optymalizacji i dodatkowej dyrektywy ScriptSock, mod_cgid
zachowuje się podobnie do mod_cgi.

Tego modułu należy używać zamiast mod_cgi zawsze, jeśli wybrano
wielowątkowy MPM.

%package mod_charset_lite
Summary:	Specify character set translation or recoding
Summary(pl.UTF-8):	Translacja lub przekodowywanie znaków
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_charset_lite.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_charset_lite) = %{version}-%{release}

%description mod_charset_lite
Specify character set translation or recoding.

This module provides a small subset of configuration mechanisms
implemented by Russian Apache and its associated mod_charset.

This is an experimental module and should be used with care.

%description mod_charset_lite -l pl.UTF-8
Translacja lub przekodowywanie znaków.

Ten moduł udostępnia niewielki podzbiór mechanizmów konfiguracyjnych
zaimplementowanych przez Russian Apache i powiązany z nim mod_charset.

Jest to moduł eksperymentalny i należy używać go z uwagą.

%package mod_dav
Summary:	Apache module - Distributed Authoring and Versioning
Summary(pl.UTF-8):	Moduł Apache'a - rozproszone autorstwo i wersjonowanie
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_dav.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	apache-mod_authn_file
Requires:	apache-mod_setenvif
Provides:	apache(mod_dav) = %{version}-%{release}

%description mod_dav
This module provides class 1 and class 2 WebDAV ('Web-based
Distributed Authoring and Versioning') functionality for Apache. This
extension to the HTTP protocol allows creating, moving, copying, and
deleting resources and collections on a remote web server.

%description mod_dav -l pl.UTF-8
Moduł udostępnia klasę 1 oraz klasę 2 WebDAV (Bazującego na WWW
rozproszonego autorstwa i wersjonowania). To rozszerzenie HTTP pozwala
na tworzenie, przesuwanie, kopiowanie oraz kasowanie zasobów na
zdalnym serwerze WWW.

%package mod_dbd
Summary:	Manages SQL database connections
Summary(pl.UTF-8):	Zarządzanie połączeniami z bazą danych SQL
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_dbd.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_dbd) = %{version}-%{release}

%description mod_dbd
mod_dbd manages SQL database connections using apr_dbd. It provides
database connections on request to modules requiring SQL database
functions, and takes care of managing databases with optimal
efficiency and scalability for both threaded and non-threaded MPMs.

%description mod_dbd -l pl.UTF-8
mod_dbd zarządza połączeniami z bazą danych SQL przy użyciu apr_dbd.
Udostępnia połączenia z bazą danych na żądanie modułów wymagających
funkcji bazy danych SQL, a następnie dba o zarządzanie bazami danych z
optymalną wydajnością i skalowalnością zarówno dla wątkowych jak i
niewątkowych MPM.

%package mod_deflate
Summary:	Apache module: Compress content before it is delivered to the client
Summary(pl.UTF-8):	Moduł Apache'a kompresujący dane przed przesłaniem ich do klienta
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_deflate.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_headers = %{version}-%{release}
Provides:	apache(mod_deflate) = %{version}-%{release}

%description mod_deflate
Compress content before it is delivered to the client.

%description mod_deflate -l pl.UTF-8
Moduł kompresujący dane przed przesłaniem ich do klienta.

%package mod_dir
Summary:	Apache module for "trailing slash" redirects and serving directory index files
Summary(pl.UTF-8):	Moduł Apache'a oferujący przekierowania i udostępnianie informacji o zawartości katalogu
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_dir.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_dir) = %{version}-%{release}
Provides:	webserver(indexfile)

%description mod_dir
This package contains mod_dir which provides "trailing slash"
redirects and serving directory index files.

%description mod_dir -l pl.UTF-8
Moduł oferujący przekierowania i udostępnianie informacji o zawartości
katalogu.

%package mod_dumpio
Summary:	Dumps all I/O to error log as desired
Summary(pl.UTF-8):	Zrzucanie całości wejścia/wyjścia do logu błędów
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_dumpio.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_dumpio) = %{version}-%{release}

%description mod_dumpio
mod_dumpio allows for the logging of all input received by Apache
and/or all output sent by Apache to be logged (dumped) to the
error.log file.

The data logging is done right after SSL decoding (for input) and
right before SSL encoding (for output). As can be expected, this can
produce extreme volumes of data, and should only be used when
debugging problems.

%description mod_dumpio -l pl.UTF-8
mod_dumpio umożliwia logowanie całego wejścia otrzymanego przez
Apache'a i/lub całęgo wyjścia wysyłanego przez Apache'a do pliku
error.log.

Logowanie danych następuja zaraz po zdekodowaniu SSL (dla wejścia) i
zaraz przed kodowaniem SSL (dla wyjścia). Jak można się spodziewać, ta
opcja może tworzyć ogromne ilości danych i powinna być używana tylko
przy diagnostyce problemów.

%package mod_echo
Summary:	A simple echo server to illustrate protocol modules
Summary(pl.UTF-8):	Prosty serwer ocho ilustrujący moduły protokołów
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_echo.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_echo) = %{version}-%{release}

%description mod_echo
This module provides an example protocol module to illustrate the
concept. It provides a simple echo server. Telnet to it and type
stuff, and it will echo it.

%description mod_echo -l pl.UTF-8
Ten moduł udostępnia przykładowy moduł protokołu ilustrujący ideę.
Udostępnia prosty serwer echo. Można się na niego zatelnetować i
napisać cokolwiek, a on odpowie tym samym.

%package mod_env
Summary:	Modifies the environment which is passed to CGI scripts and SSI pages
Summary(pl.UTF-8):	Modyfikowanie środowiska przekazywanego skryptom CGI i stronom SSI
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_env.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_env) = %{version}-%{release}
Provides:	webserver(setenv)

%description mod_env
This module allows for control of the environment that will be
provided to CGI scripts and SSI pages. Environment variables may be
passed from the shell which invoked the httpd process. Alternatively,
environment variables may be set or unset within the configuration
process.

%description mod_env -l pl.UTF-8
Ten moduł pozwala na kontrolę środowiska udostępnianego skryptom CGI i
stronom SSI. Zmienne środowiskowe mogą być przekazywane z powłoki w
czasie uruchamiania procesu httpd, albo - alternatywnie - ustawiane i
usuwane w procesie konfiguracji.

%package mod_expires
Summary:	Apache module which generates Expires HTTP headers
Summary(pl.UTF-8):	Moduł Apache'a generujący nagłówki HTTP Expires
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_expires.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_expires) = %{version}-%{release}
Provides:	webserver(expires)

%description mod_expires
This module controls the setting of the Expires HTTP header in server
responses. The expiration date can set to be relative to either the
time the source file was last modified, or to the time of the client
access.

%description mod_expires -l pl.UTF-8
Moduł kontroluje ustawianie nagłówka HTTP Expires. Data wygaśnięcia
ważności może być ustalana w zależności od czasu modyfikacji plików
źródłowych lub odwołania klienta.

%package mod_ext_filter
Summary:	Pass the response body through an external program before delivery to the client
Summary(pl.UTF-8):	Przekazywanie ciała odpowiedzi do zewnętrznego programu przed przekazaniem klientowi
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_ext_filter.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_ext_filter) = %{version}-%{release}

%description mod_ext_filter
mod_ext_filter presents a simple and familiar programming model for
filters. With this module, a program which reads from stdin and writes
to stdout (i.e., a Unix-style filter command) can be a filter for
Apache.

This filtering mechanism is much slower than using a filter which is
specially written for the Apache API and runs inside of the Apache
server process, but it does have the following benefits:
- the programming model is much simpler
- any programming/scripting language can be used, provided that it
  allows the program to read from standard input and write to standard
  output
- existing programs can be used unmodified as Apache filters

Even when the performance characteristics are not suitable for
production use, mod_ext_filter can be used as a prototype environment
for filters.

%description mod_ext_filter -l pl.UTF-8
mod_ext_filter przedstawia prosty i przyjazny model programowania dla
filtrów. Przy użyciu tego modułu program czytający ze standardowego
wejścia i piszący na standardowe wyjście (czyli uniksowe polecenie
filtrujące) może być filtrem dla Apache'a.

Ten mechanizm filtrujący jest znacznie wolniejszy niż użycie filtru
napisanego specjalnie dla API Apache'a i działającego wewnątrz procesu
Apache'a, ale ma następujące zalety:
- znacznie prostszy model programowania
- możliwość użycia dowolnego języka programowania/skryptowego, jeśli
  tylko umożliwia czytanie ze standardowego wejścia i pisanie na
  standardowe wyjście
- możliwość użycia istniejących programów bez modyfikacji jako filtrów
  Apache'a.

Nawet kiedy charakterystyka wydajności nie jest odpowiednia dla użytku
produkcyjnego, mod_ext_filter można używać w środowisku prototypowym
dla filtrów.

%package mod_file_cache
Summary:	Apache module: caches a static list of files in memory
Summary(pl.UTF-8):	Moduł Apache'a cache'ujący statyczną listę plików w pamięci
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_file_cache.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_file_cache) = %{version}-%{release}
Obsoletes:	apache-mmap_static

%description mod_file_cache
Caches a static list of files in memory.

This module is an extension of and borrows heavily from the
mod_mmap_static module in Apache 1.3.

%description mod_file_cache -l pl.UTF-8
Moduł cache'ujący statyczną listę plików w pamięci.

%package mod_filter
Summary:	Context-sensitive smart filter configuration module
Summary(pl.UTF-8):	Moduł inteligentnej, zależnej od kontekstu konfiguracji filtrów
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_filter.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_filter) = %{version}-%{release}

%description mod_filter
This module enables smart, context-sensitive configuration of output
content filters. For example, apache can be configured to process
different content-types through different filters, even when the
content-type is not known in advance (e.g. in a proxy).

%description mod_filter -l pl.UTF-8
Ten moduł umożliwia inteligentne, zależne od kontekstu konfigurowanie
wyjściowych filtrów treści. Na przykład, Apache'a można skonfigurować
do przetwarzania różnych content-type poprzez różne filtry, nawet
jeśli content-type nie jest znany z góry (np. w wypadku proxy).

%package mod_headers
Summary:	Apache module allows for the customization of HTTP response headers
Summary(pl.UTF-8):	Moduł Apache'a pozwalający na modyfikację nagłówków HTTP
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_headers.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_headers) = %{version}-%{release}

%description mod_headers
This package contains mod_headers module. The module allows for the
customization of HTTP response headers. Headers can be merged,
replaced or removed.

%description mod_headers -l pl.UTF-8
Moduł pozwalający na łączenie, usuwanie oraz zamianę nagłówków HTTP
wysyłanych do przeglądarki.

%package mod_ident
Summary:	RFC 1413 ident lookups
Summary(pl.UTF-8):	Sprawdzanie identyfikacji RFC 1413
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_ident.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_ident) = %{version}-%{release}

%description mod_ident
This module queries an RFC 1413 compatible daemon on a remote host to
look up the owner of a connection.

%description mod_ident -l pl.UTF-8
Ten moduł odpytuje demona zgodnego z RFC 1413 na zdalnym hoście w celu
sprawdzenia właściciela połączenia.

%package mod_imagemap
Summary:	Server-side imagemap processing
Summary(pl.UTF-8):	Przetwarzanie map obrazów po stronie serwera
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_imagemap.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_imagemap) = %{version}-%{release}
Provides:	apache-mod_imap
Obsoletes:	apache-mod_imap

%description mod_imagemap
This module processes .map files, thereby replacing the functionality
of the imagemap CGI program. Any directory or document type configured
to use the handler imap-file (using either AddHandler or SetHandler)
will be processed by this module.

%description mod_imagemap -l pl.UTF-8
Ten moduł przetwarza pliki .map zastępując funkcjonalność programu CGI
imagemap. Dowolny katalog lub rodzaj dokumentu skonfigurowany do
używania procedury obsługi imap-file (poprzez AddHandler lub
SetHandler) będzie przetwarzany przez ten moduł.

%package mod_include
Summary:	Server-parsed html documents (Server Side Includes)
Summary(pl.UTF-8):	Dokumenty przetwarzane przez serwer (Server Side Includes)
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_include.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_include) = %{version}-%{release}

%description mod_include
This module provides a filter which will process files before they are
sent to the client. The processing is controlled by specially
formatted SGML comments, referred to as elements. These elements allow
conditional text, the inclusion of other files or programs, as well as
the setting and printing of environment variables.

%description mod_include -l pl.UTF-8
Ten moduł dostarcza procedurę obsługi przetwarzającą pliki przed
wysłaniem ich do klienta. Przetwarzanie jest sterowane specjalnie
sformatowanymi komentarzami SGML, nazywanymi elementami. Elementy te
pozwalają na tekst warunkowy, dołączanie innych plików lub programów,
a także ustawianie i wypisywanie zmiennych środowiskowych.

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Summary(pl.UTF-8):	Moduł Apache'a udostępniający informacje o serwerze
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_info.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Provides:	apache(mod_info) = %{version}-%{release}

%description mod_info
This package contains mod_info module. It provides a comprehensive
overview of the server configuration including all installed modules
and directives in the configuration files.

%description mod_info -l pl.UTF-8
Moduł udostępniający informacje o konfiguracji serwera,
zainstalowanych modułach itp.

%package mod_ldap
Summary:	Apache module for LDAP connection pooling and result caching services for other LDAP modules
Summary(pl.UTF-8):	Moduł Apache'a zarządzający połączeniami z serwerami LDAP
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_ldap.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_ldap) = %{version}-%{release}

%description mod_ldap
This module was created to improve the performance of websites relying
on backend connections to LDAP servers. In addition to the functions
provided by the standard LDAP libraries, this module adds an LDAP
connection pool and an LDAP shared memory cache.

%description mod_ldap -l pl.UTF-8
Moduł Apache'a poprawiający wydajność serwisów polegających na
połączeniach z serwerami LDAP. Oprócz funkcjo udostępnianych przez
standardowe biblioteki LDAP ten moduł dodaje zarządzanie pulą połączeń
i współdzieloną pamięć podręczną zapytań.

%package mod_log_config
Summary:	Logging of the requests made to the server
Summary(pl.UTF-8):	Logowanie żądań zgłaszanych do serwera
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_log_config.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_log_config) = %{version}-%{release}
Provides:	webserver(log)

%description mod_log_config
This module provides for flexible logging of client requests. Logs are
written in a customizable format, and may be written directly to a
file, or to an external program. Conditional logging is provided so
that individual requests may be included or excluded from the logs
based on characteristics of the request.

%description mod_log_config -l pl.UTF-8
Ten moduł umożliwia elastyczne logowanie żądań klientów. Logi są
zapisywane w konfigurowalnym formacie i mogą być zapisywane
bezpośrednio do pliku lub przekazywane do zewnętrznego programu.
Dostępne jest logowanie warunkowe polegające na włączeniu lub
wyłączeniu poszczególnych żądań z logowania na podstawie
charakterystyki żądania.

%package mod_log_forensic
Summary:	Forensic Logging of the requests made to the server
Summary(pl.UTF-8):	Logowanie żadań zgłaszanych do serwera w celu późniejszej analizy
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_log_forensic.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_log_forensic) = %{version}-%{release}

%description mod_log_forensic
This module provides for forensic logging of client requests. Logging
is done before and after processing a request, so the forensic log
contains two log lines for each request.

%description mod_log_forensic -l pl.UTF-8
Ten moduł pozwala na logowanie żądań w celu późniejszej analizy.
Logowanie jest wykonywane przed i po przetworzeniu żądania, więc log
zawiera dwie linie dla każdego żądania.

%package mod_logio
Summary:	Logging of input and output bytes per request
Summary(pl.UTF-8):	Logowanie liczby bajtów wejścia i wyjścia dla zapytań
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_logio.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_log_config = %{version}-%{release}
Provides:	apache(mod_logio) = %{version}-%{release}

%description mod_logio
This module provides the logging of input and output number of bytes
received/sent per request. The numbers reflect the actual bytes as
received on the network, which then takes into account the headers and
bodies of requests and responses. The counting is done before SSL/TLS
on input and after SSL/TLS on output, so the numbers will correctly
reflect any changes made by encryption.

%description mod_logio -l pl.UTF-8
Ten moduł zapewnia logowanie liczby bajtów wejścia i wyjścia
odbieranych/wysyłanych przy każdym zapytaniu. Liczby odzwierciedlają
rzeczywiste bajty przesyłane przez sieć, z wliczonymi nagłówkami i
ciałami żądań i odpowiedzi. Zliczanie jest wykonywane przed SSL/TLS na
wejściu i po SSL/TLS na wyjściu, więc liczby będą właściwie
odzwierciedlały wszystkie zmiany dokonywane przez szyfrowanie.

%package mod_mime
Summary:	Associates the requested filename's extensions with the file's behavior and content
Summary(pl.UTF-8):	Wiązanie określonych rozszerzeń plików z zachowaniem i zawartością
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_mime.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	mailcap
Provides:	apache(mod_mime) = %{version}-%{release}

%description mod_mime
This module is used to associate various bits of "meta information"
with files by their filename extensions. This information relates the
filename of the document to it's mime-type, language, character set
and encoding. This information is sent to the browser, and
participates in content negotiation, so the user's preferences are
respected when choosing one of several possible files to serve. See
mod_negotiation for more information about content negotiation.

%description mod_mime -l pl.UTF-8
Ten moduł służy do wiązania określonych części "metainformacji" z
plikami w zależności od rozszerzeń nazw plików. Informacje te łączą
nazwy plików dokumentów z ich typem MIME, językiem, zestawem znaków i
kodowaniem. Informacje te są wysyłane przeglądarce i mają wpływ na
negocjację treści, tak że preferencje użytkownika są respektowane przy
wybieraniu jednego z kilku dostępnych do zaserwowania. Więcej
informacji o negocjacji treści jest w dokumentacji do mod_negotiation.

%package mod_mime_magic
Summary:	Determines the MIME type of a file by looking at a few bytes of its contents
Summary(pl.UTF-8):	Określanie typu MIME pliku poprzez sprawdzanie kilku bajtów jego zawartości
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_mime_magic.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	file
Provides:	apache(mod_mime_magic) = %{version}-%{release}

%description mod_mime_magic
This module determines the MIME type of files in the same way the Unix
file(1) command works: it looks at the first few bytes of the file. It
is intended as a "second line of defense" for cases that mod_mime
can't resolve.

%description mod_mime_magic -l pl.UTF-8
Ten moduł określa typ MIME plików w ten sam sposób, co uniksowe
polecenie file(1): patrzy na kilka początkowych bajtów pliku. Ma
służyć jako "druga linia obrony" dla przypadków, których nie może
rozwiązać mod_mime.

%package mod_negotiation
Summary:	Provides for content negotiation
Summary(pl.UTF-8):	Moduł do negocjacji treści
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_negotiation.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_mime = %{version}-%{release}
Provides:	apache(mod_negotiation) = %{version}-%{release}

%description mod_negotiation
Content negotiation, or more accurately content selection, is the
selection of the document that best matches the clients capabilities,
from one of several available documents.

%description mod_negotiation -l pl.UTF-8
Negocjacja treści, lub bardziej precyzyjnie - wybór treści, to wybór
dokumentu najbardziej odpowiadającego możliwościom klientów spośród
kilku możliwych dokumentów.

%package mod_proxy
Summary:	Apache module with Web proxy
Summary(pl.UTF-8):	Moduł Apache'a dodający obsługę serwera proxy
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_proxy.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Provides:	apache(mod_proxy) = %{version}-%{release}

%description mod_proxy
This package contains module with implementation a proxy/cache for
Apache. It implements proxying capability for FTP, CONNECT (for SSL),
HTTP/0.9, HTTP/1.0 and HTTP/1.1. The module can be configured to
connect to other proxy modules for these and other protocols.

%description mod_proxy -l pl.UTF-8
Moduł zawiera implementację serwera proxy/cache dla Apache.
Implementacja zawiera obsługę FTP, CONNECT (dla SSL), HTTP/0.9,
HTTP/1.0 i HTTP/1.1.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Summary(pl.UTF-8):	Moduł Apache'a do "przepisywania" adresów URL w locie
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_rewrite) = %{version}-%{release}

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to
rewrite requested URLs on the fly.

%description mod_rewrite -l pl.UTF-8
Moduł oferujący możliwość "przepisywania" adresów URL w locie.

%package mod_setenvif
Summary:	Allows the setting of environment variables based on characteristics of the request
Summary(pl.UTF-8):	Ustawianie zmiennych środowiskowych w oparciu o charakterystykę żądania
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_setenvif.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_setenvif) = %{version}-%{release}

%description mod_setenvif
The mod_setenvif module allows you to set environment variables
according to whether different aspects of the request match regular
expressions you specify. These environment variables can be used by
other parts of the server to make decisions about actions to be taken.

%description mod_setenvif -l pl.UTF-8
Moduł mod_setenvif pozwala na ustawianie zmiennych środowiskowych w
zależności od różnych aspektów żądania pasujących do podanych wyrażeń
regularnych. Te zmienne środowiskowe mogą być używane przez inne
części serwera do podejmowania decyzji o podejmowanych akcjach.

%package mod_speling
Summary:	Attempts to correct mistaken URLs by ignoring capitalization and by allowing up to one misspelling
Summary(pl.UTF-8):	Próba poprawiania błędnych URL-i poprzez ignorowanie wielkości liter i zezwalanie na jedną literówkę
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_speling.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_speling) = %{version}-%{release}

%description mod_speling
Requests to documents sometimes cannot be served by the core apache
server because the request was misspelled or miscapitalized. This
module addresses this problem by trying to find a matching document,
even after all other modules gave up. It does its work by comparing
each document name in the requested directory against the requested
document name without regard to case, and allowing up to one
misspelling (character insertion / omission / transposition or wrong
character). A list is built with all document names which were matched
using this strategy.

%description mod_speling -l pl.UTF-8
Czasami żądania dokumentów nie mogą być wykonane przez sam serwer
Apache, ponieważ żądanie zostało napisane z błędem w znakach lub
wielkości liter. Ten moduł próbuje rozwiązać ten problem próbując
znaleźć pasujący dokument, nawet jeśli inne moduły się poddały. Działa
on poprzez porównywanie nazwy każdego dokumentu w żądanym katalogu z
żądaną nazwą dokumentu bez zwracania uwagi na wielkość liter i
pozwalając na jeden błąd (dodany, pominięty, przestawiony lub zły
znak). Tworzona jest lista dla wszystkich nazw dokumentów pasujących
dla tej strategii.

%package mod_ssl
Summary:	SSL/TLS module for the Apache HTTP server
Summary(pl.UTF-8):	Moduł SSL/TSL dla serwera Apache
Summary(ru.UTF-8):	Модуль SSL/TLS для веб-сервера Apache
Epoch:		1
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_ssl.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_ssl) = 1:%{version}-%{release}

%description mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer Security
(TLS) protocols.

%description mod_ssl -l pl.UTF-8
Moduł mod_ssl udostępnia wsparcie do silnej kryptografii dla serwera
Apache poprzez protokoły SSL/TSL (Secure Sockets Layer/Transport Layer
Security).

%description mod_ssl -l ru.UTF-8
Модуль mod_ssl обеспечивает поддержку в веб-сервере Apache надежного
шифрования средствами Secure Sockets Layer (SSL) и Transport Layer

%package mod_status
Summary:	Server status report module for Apache
Summary(pl.UTF-8):	Moduł udostępniający informacje statystyczne z serwera Apache
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_status.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Provides:	apache(mod_status) = %{version}-%{release}

%description mod_status
The Status module allows a server administrator to find out how well
their server is performing. A HTML page is presented that gives the
current server statistics in an easily readable form. If required this
page can be made to automatically refresh (given a compatible
browser).

%description mod_status -l pl.UTF-8
Moduł pozwala administratorowi na przeglądanie statystyk dotyczących
pracy serwera Apache (w postaci strony HTML).

%package mod_substitute
Summary:	Substitute module for Apache
Summary(pl.UTF-8):	Moduł pozwalający na znajdywanie i zastępowanie wyjścia dla serwera Apache
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_substitute.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_substitute) = %{version}-%{release}

%description mod_substitute
The Substitute module provides a mechanism to perform both regular
expression and fixed string substitutions on response bodies.

%description mod_substitute -l pl.UTF-8
Moduł pozwala na zastępowanie ciągów znaków w wyjściu również na
podstawie wyrażenia regularnego.

%package mod_unique_id
Summary:	Apache module which provides a magic token for each request
Summary(pl.UTF-8):	Moduł Apache'a nadający każdemu zapytaniu unikalny token
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_unique_id.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_unique_id) = %{version}-%{release}

%description mod_unique_id
This package contains the mod_unique_id. This module provides a magic
token for each request which is guaranteed to be unique across "all"
requests under very specific conditions. The unique identifier is even
unique across multiple machines in a properly configured cluster of
machines. The environment variable UNIQUE_ID is set to the identifier
for each request. Unique identifiers are useful for various reasons
which are beyond the scope of this document.

%description mod_unique_id -l pl.UTF-8
Moduł nadaje każdemu zapytaniu token unikalny w ramach wszystkich
zapytań, nawet w ramach poprawnie skonfigurowanego klastra z wielu
maszyn. Moduł ustawia przy każdym zapytaniu zmienną środowiskową
UNIQUE_ID.

%package mod_userdir
Summary:	User-specific directories
Summary(pl.UTF-8):	Katalogi specyficzne dla użytkowników
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_userdir.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Provides:	apache(mod_userdir) = %{version}-%{release}

%description mod_userdir
This module allows user-specific directories to be accessed using the
http://example.com/~user/ syntax.

%description mod_userdir -l pl.UTF-8
Ten moduł pozwala na dostęp do katalogów specyficznych dla
użytkowników przy użyciu składni http://example.com/~user/ .

%package mod_usertrack
Summary:	Apache module for user tracking using cookies
Summary(pl.UTF-8):	Moduł Apache'a służący do śledzenia "ciasteczek"
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_usertrack.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_usertrack) = %{version}-%{release}

%description mod_usertrack
This package contains the user tracking module which did its own
logging using CookieLog directory. This module allow multiple log
files.

%description mod_usertrack -l pl.UTF-8
Ten pakiet zawiera moduł śledzący użytkowników zapisujący własny log
przy użyciu katalogu CookieLog. Pozwala na użycie wielu plików logów.

%package mod_version
Summary:	Version dependent configuration
Summary(pl.UTF-8):	Konfiguracja zależna od wersji
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_version.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_version) = %{version}-%{release}

%description mod_version
This module is designed for the use in test suites and large networks
which have to deal with different httpd versions and different
configurations. It provides a new container -- <IfVersion>, which
allows a flexible version checking including numeric comparisons and
regular expressions.

%description mod_version -l pl.UTF-8
Ten moduł jest przeznaczony do używania w zestawach testów i dużych
sieciach, gdzie trzeba inaczej obsługiwać różne wersje httpd i różne
konfiguracje. Udostępnia nowy kontener: <IfVersion>, umożliwiający
elastyczne sprawdzanie wersji włącznie z porównaniami liczbowymi i
wyrażeniami regularnymi.

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Summary(pl.UTF-8):	Moduł Apache'a dodający obsługę hostów wirtualnych
Group:		Networking/Daemons/HTTP
URL:		http://httpd.apache.org/docs/2.2/mod/mod_vhost_alias.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_vhost_alias) = %{version}-%{release}

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

%description mod_vhost_alias -l pl.UTF-8
Moduł umożliwia na dynamiczne konfigurowanie masowej ilości serwerów
wirtualnych.

%package -n htpasswd-%{name}
Summary:	Apache 2 htpasswd utility: manage user files for basic authentication
Summary(pl.UTF-8):	Narzędzie htpasswd z Apache'a 2 do zarządzania plikami uwierzytelnienia basic
Group:		Networking/Utilities
Provides:	htpasswd
Obsoletes:	htpasswd

%description -n htpasswd-%{name}
htpasswd is used to create and update the flat-files used to store
usernames and password for basic authentication of HTTP users. This
package contains htpasswd from Apache 2; this version supports
plaintext passwords and CRYPT (default), MD5 and SHA1 encryptions.

%description -n htpasswd-%{name} -l pl.UTF-8
htpasswd służy do tworzenia i uaktualniania plików tekstowych
służących do przechowywania nazw użytkowników i haseł do podstawowego
uwierzytelnienia użytkowników HTTP. Ten pakiet zawiera htpasswd z
Apache'a 2; ta wersja obsługuje hasła zapisane czystym tekstem oraz
zakodowane algorytmami CRYPT (domyślnym), MD5 i SHA1.

%package dbmtools
Summary:	Apache 2 tools for manipulating DBM files
Summary(pl.UTF-8):	Narzędzia Apache'a 2 do obróbki plików DBM
Group:		Networking/Utilities
Requires:	%{name}-base = %{version}-%{release}

%description dbmtools
Apache 2 tools for manipulating DBM files.

%description dbmtools -l pl.UTF-8
Narzędzia Apache'a 2 do obróbki plików DBM.

%package cgi_test
Summary:	cgi test/demo programs
Summary(pl.UTF-8):	Programy testowe/przykładowe cgi
Group:		Networking/Utilities
Requires:	%{name}-base = %{version}-%{release}
Requires:	filesystem >= 2.0-1

%description cgi_test
Two cgi test/demo programs: test-cgi and print-env.

%description cgi_test -l pl.UTF-8
Dwa programy testowe/przykładowe cgi: test-cgi and print-env.

%prep
%setup -q -n httpd-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch23 -p1
%patch24 -p1

# using system apr, apr-util and pcre
rm -rf srclib/{apr,apr-util,pcre}

# sanity check
MODULES_API=`awk '/#define MODULE_MAGIC_NUMBER_MAJOR/ {print $3}' include/ap_mmn.h`
if [ "$MODULES_API" != "%_apache_modules_api" ]; then
	echo "Set %%_apache_modules_api to $MODULES_API and rerun."
	exit 1
fi

# fix libdir (at least in PLD layout; no need to care about other ones)
sed -i -e 's,/lib$,/%{_lib},' config.layout

%build
cp /usr/share/apr/build/apr_common.m4 build
%{__libtoolize}
%{__aclocal} -I build
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
for mpm in prefork worker %{?with_metuxmpm:metuxmpm} %{?with_peruser:peruser} %{?with_event:event}; do
install -d "buildmpm-${mpm}"; cd "buildmpm-${mpm}"
../%configure \
	--enable-layout=PLD \
	--disable-v4-mapped \
	$( [ "${mpm}" = "prefork" -o "${mpm}" = "worker" -o "${mpm}" = "event" ] && echo "--enable-exception-hook" ) \
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
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT%{_var}/{log/{httpd,archive/httpd},{run,cache}/httpd,lock/mod_dav} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{webapps.d,conf.d} \
	$RPM_BUILD_ROOT%{_datadir}/cgi-bin

# prefork is default one
%{__make} -C buildmpm-prefork install \
	DESTDIR=$RPM_BUILD_ROOT

# install other mpm-s
for mpm in %{?with_metuxmpm:metuxmpm} %{?with_peruser:peruser} worker %{?with_event:event}; do
	install buildmpm-${mpm}/httpd.${mpm} $RPM_BUILD_ROOT%{_sbindir}/httpd.${mpm}
done

ln -s httpd.prefork $RPM_BUILD_ROOT%{_sbindir}/httpd
ln -s %{_libexecdir} $RPM_BUILD_ROOT%{_sysconfdir}/modules
ln -s %{_localstatedir}/run/httpd $RPM_BUILD_ROOT%{_sysconfdir}/run
ln -s %{_var}/log/httpd $RPM_BUILD_ROOT%{_sysconfdir}/logs
ln -s conf.d $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/httpd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/httpd

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,agent,referer,suexec}_log

%if %{with ssl}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ssl
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/server.crt
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/server.key
%endif

install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

CFG="$RPM_BUILD_ROOT%{_sysconfdir}/conf.d/"

install %{SOURCE7} $CFG/10_common.conf

install %{SOURCE23} $CFG/01_mod_mime.conf
install %{SOURCE24} $CFG/01_mod_authz_host.conf
install %{SOURCE25} $CFG/01_mod_cgid.conf
install %{SOURCE26} $CFG/01_mod_log_config.conf
install %{SOURCE27} $CFG/01_mod_mime_magic.conf
install %{SOURCE28} $CFG/01_mod_cache.conf
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
install %{SOURCE18} $CFG/30_errordocs.conf
install %{SOURCE19} $CFG/30_manual.conf
install %{SOURCE20} $CFG/16_mod_userdir.conf
install %{SOURCE21} $CFG/10_mpm.conf
install %{SOURCE22} $CFG/20_languages.conf

echo "LoadModule alias_module modules/mod_alias.so" > $CFG/00_mod_alias.conf
echo "LoadModule authn_file_module	modules/mod_authn_file.so" > $CFG/00_mod_authn_file.conf
echo "LoadModule authn_dbm_module	modules/mod_authn_dbm.so" > $CFG/00_mod_authn_dbm.conf
echo "LoadModule authn_anon_module	modules/mod_authn_anon.so" > $CFG/00_mod_authn_anon.conf
echo "LoadModule authn_dbd_module	modules/mod_authn_dbd.so" > $CFG/00_mod_authn_dbd.conf
echo "LoadModule authn_default_module	modules/mod_authn_default.so" > $CFG/00_mod_authn_default.conf
echo "LoadModule authn_alias_module	modules/mod_authn_alias.so" > $CFG/00_mod_authn_alias.conf
echo "LoadModule authz_groupfile_module	modules/mod_authz_groupfile.so" > $CFG/00_mod_authz_groupfile.conf
echo "LoadModule authz_user_module	modules/mod_authz_user.so" > $CFG/00_mod_authz_user.conf
echo "LoadModule authz_dbm_module	modules/mod_authz_dbm.so" > $CFG/00_mod_authz_dbm.conf
echo "LoadModule authz_owner_module	modules/mod_authz_owner.so" > $CFG/00_mod_authz_owner.conf
echo "LoadModule authnz_ldap_module	modules/mod_authnz_ldap.so" > $CFG/00_mod_authnz_ldap.conf
echo "LoadModule authz_default_module	modules/mod_authz_default.so" > $CFG/00_mod_authz_default.conf
echo "LoadModule auth_basic_module	modules/mod_auth_basic.so" > $CFG/00_mod_auth_basic.conf
echo "LoadModule dbd_module	modules/mod_dbd.so" > $CFG/00_mod_dbd.conf
%if %{with bucketeer}
echo "LoadModule bucketeer_module	modules/mod_bucketeer.so" > $CFG/00_mod_bucketeer.conf
%endif
echo "LoadModule dumpio_module	modules/mod_dumpio.so" > $CFG/00_mod_dumpio.conf
echo "LoadModule echo_module	modules/mod_echo.so" > $CFG/00_mod_echo.conf
echo "LoadModule case_filter_module	modules/mod_case_filter.so" > $CFG/00_mod_case_filter.conf
echo "LoadModule case_filter_in_module	modules/mod_case_filter_in.so" > $CFG/00_mod_case_filter_in.conf
echo "LoadModule ext_filter_module	modules/mod_ext_filter.so" > $CFG/00_mod_ext_filter.conf
echo "LoadModule include_module	modules/mod_include.so" > $CFG/00_mod_include.conf
echo "LoadModule filter_module	modules/mod_filter.so" > $CFG/00_mod_filter.conf
echo "LoadModule log_forensic_module	modules/mod_log_forensic.so" > $CFG/00_mod_log_forensic.conf
echo "LoadModule logio_module	modules/mod_logio.so" > $CFG/00_mod_logio.conf
echo "LoadModule env_module	modules/mod_env.so" > $CFG/00_mod_env.conf
echo "LoadModule cern_meta_module	modules/mod_cern_meta.so" > $CFG/00_mod_cern_meta.conf
echo "LoadModule ident_module	modules/mod_ident.so" > $CFG/00_mod_ident.conf
echo "LoadModule setenvif_module	modules/mod_setenvif.so" > $CFG/00_mod_setenvif.conf
echo "LoadModule version_module	modules/mod_version.so" > $CFG/00_mod_version.conf
echo "LoadModule asis_module	modules/mod_asis.so" > $CFG/00_mod_asis.conf
echo "LoadModule cgi_module	modules/mod_cgi.so" > $CFG/00_mod_cgi.conf
echo "LoadModule negotiation_module	modules/mod_negotiation.so" > $CFG/00_mod_negotiation.conf
echo "LoadModule imagemap_module	modules/mod_imagemap.so" > $CFG/00_mod_imagemap.conf
echo "LoadModule speling_module	modules/mod_speling.so" > $CFG/00_mod_speling.conf
echo "LoadModule ldap_module	modules/mod_ldap.so" > $CFG/00_mod_ldap.conf
echo "LoadModule actions_module	modules/mod_actions.so" > $CFG/00_mod_actions.conf
echo "LoadModule auth_digest_module	modules/mod_auth_digest.so" > $CFG/00_mod_auth_digest.conf
echo "LoadModule charset_lite_module	modules/mod_charset_lite.so" > $CFG/00_mod_charset_lite.conf
echo "LoadModule expires_module	modules/mod_expires.so" > $CFG/00_mod_expires.conf
echo "LoadModule file_cache_module	modules/mod_file_cache.so" > $CFG/00_mod_file_cache.conf
echo "LoadModule headers_module	modules/mod_headers.so" > $CFG/00_mod_headers.conf
echo "LoadModule rewrite_module	modules/mod_rewrite.so" > $CFG/00_mod_rewrite.conf
echo "LoadModule usertrack_module	modules/mod_usertrack.so" > $CFG/00_mod_usertrack.conf
echo "LoadModule unique_id_module	modules/mod_unique_id.so" > $CFG/00_mod_unique_id.conf
echo "LoadModule substitute_module	modules/mod_substitute.so" > $CFG/00_mod_substitute.conf

# anything in style dir not ending with .css is trash
rm -rf $RPM_BUILD_ROOT%{_datadir}/manual/style/{lang,latex,xsl}
find $RPM_BUILD_ROOT%{_datadir}/manual/style -type f ! -name '*.css' -print0 | xargs -0r rm -f

# find manual files
> manual.files
cur=$(pwd)
cd $RPM_BUILD_ROOT
find ./%{_datadir}/manual -type d -printf "%%%%dir %{_datadir}/manual/%%P\n" >> "$cur/manual.files"
find ./%{_datadir}/manual -type f -printf "%{_datadir}/manual/%%P\n" | sed -e '
s/^.*\.\(de\|es\|fr\|ja\|ko\|ru\)\(\..*\)\?/%%lang(\1) &/
s/^.*\.\(pt-br\)/%%lang(pt_BR) &/
' >> "$cur/manual.files"
cd $cur

# htpasswd goes to %{_bindir}
mv $RPM_BUILD_ROOT%{_sbindir}/htpasswd $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_bindir}/htpasswd $RPM_BUILD_ROOT%{_sbindir}

# cgi_test: create config file with ScriptAlias
cat << 'EOF' > $CFG/09_cgi_test.conf
ScriptAlias /cgi-bin/printenv %{_cgibindir}/printenv
ScriptAlias /cgi-bin/test-cgi %{_cgibindir}/test-cgi
EOF

# our suexec is patched to support php + fcgi + suexec with
# virtual users when called as suexec.fcgi
ln -sf suexec $RPM_BUILD_ROOT%{_sbindir}/suexec.fcgi

# no value
rm $RPM_BUILD_ROOT%{_libexecdir}/build/config.nice
rm $RPM_BUILD_ROOT%{_libexecdir}/*.exp
rm $RPM_BUILD_ROOT%{_sysconfdir}/mime.types
rm $RPM_BUILD_ROOT%{_sysconfdir}/httpd.prefork.conf
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/{extra,original}

%clean
rm -rf $RPM_BUILD_ROOT

%pre base
%groupadd -g 51 http
%useradd -u 51 -r -d /home/services/httpd -s /bin/false -c "HTTP User" -g http http

%pretrans base
# change httpd.conf from dir to symlink
if [ ! -L /etc/httpd/httpd.conf ]; then
	if [ -d /etc/httpd/httpd.conf ]; then
		if [ -d /etc/httpd/conf.d ]; then
			mv /etc/httpd/httpd.conf/* /etc/httpd/conf.d
			rmdir /etc/httpd/httpd.conf 2>/dev/null || mv -v /etc/httpd/httpd.conf{,.rpmsave}
		else
			mv /etc/httpd/httpd.conf /etc/httpd/conf.d
		fi

		# new module packages issue error as first installed over 2.0 installation
		mv -f /var/lock/subsys/httpd{,.disabled} 2>/dev/null
	fi

	# always have httpd.conf symlink (until all packages from Ac use new dir)
	install -d /etc/httpd
	ln -s conf.d /etc/httpd/httpd.conf
fi
exit 0

%post base
/sbin/chkconfig --add httpd
umask 137
touch /var/log/httpd/{access,error,agent,referer}_log

%preun base
if [ "$1" = "0" ]; then
	%service httpd stop
	/sbin/chkconfig --del httpd
fi

%postun base
if [ "$1" = "0" ]; then
	%userremove http
	%groupremove http
fi

%triggerpostun base -- %{name} < 2.0.50-6.9
%banner %{name}-2.0.50-6 << EOF
WARNING!!!
Since apache-2.0.50-6 autoindex module has been separated to package
%{name}-mod_autoindex If you want to have the same functionality do:
poldek -Uv %{name}-mod_autoindex
EOF

%triggerpostun base -- %{name} < 2.0.54-4
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

%triggerpostun base -- %{name} < 2.0.55-3.1
# check for config first as in 2.2 it's .rpmsave
if [ -f /etc/httpd/httpd.conf/10_httpd.conf ]; then
	if ! grep -q 'Include webapps.d/' /etc/httpd/httpd.conf/10_httpd.conf; then
		# make sure webapps.d is included
		cp -f /etc/httpd/httpd.conf/10_httpd.conf{,.rpmsave}
		# this file is ugly, so just append new lines
		cat <<-EOF >> /etc/httpd/httpd.conf/10_httpd.conf
		# Include webapps config
		Include webapps.d/*.conf
EOF
	fi
fi

%triggerpostun base -- %{name} < 2.2.0
# change HTTPD_CONF to point to new location. *only* if it's the
# default config setting
cp -f /etc/sysconfig/httpd{,.rpmorig}
sed -i -e '/^HTTPD_CONF="\/etc\/httpd\/httpd.conf"/s,.*,HTTPD_CONF="/etc/httpd/apache.conf",' /etc/sysconfig/httpd

if [ -f /etc/httpd/conf.d/10_httpd.conf.rpmsave ]; then
	sed -e '
	# as separate modules
	/^LoadModule access_module/s,^,#,
	/^LoadModule alias_module/s,^,#,
	/^LoadModule asis_module/s,^,#,
	/^LoadModule cern_meta_module/s,^,#,
	/^LoadModule cgi_module/s,^,#,
	/^LoadModule env_module/s,^,#,
	/^LoadModule include_module/s,^,#,
	/^LoadModule log_config_module/s,^,#,
	/^LoadModule mime_magic_module/s,^,#,
	/^LoadModule mime_module/s,^,#,
	/^LoadModule negotiation_module/s,^,#,
	/^LoadModule setenvif_module/s,^,#,
	/^LoadModule speling_module/s,^,#,
	/^LoadModule userdir_module/s,^,#,

	# in 30_errordocs.conf
	/<IfModule mod_include.c>/,/<\/IfModule>/s,^,#,

	# in 57_mod_autoindex.conf
	/^Alias \/icons\//s,^,#,

	# in apache.conf
	/^ScriptAlias \/cgi-bin\//s,^,#,
	/^Listen 80/s,^,#,

	# avoid loops
	/Include conf.d\/\*.conf/s,^,#,
	/Include webapps.d\/\*.conf/s,^,#,

	' < /etc/httpd/conf.d/10_httpd.conf.rpmsave > /etc/httpd/conf.d/10_httpd.conf
fi

%banner -e %{name} <<'EOF'
NB! Apache main config has been changed to /etc/httpd/apache.conf

There has been changed a lot, so many things could be broken.
Please report bugs to <http://bugs.pld-linux.org/>.

EOF

%triggerpostun mod_ssl -- %{name}-mod_ssl < 1:2.2.0-3.1
cp -f /etc/httpd/conf.d/40_mod_ssl.conf{,.rpmsave}
sed -i -e '
	s,/var/run/apache,/var/run/httpd,g
	s,/var/cache/apache,/var/cache/httpd,g
' /etc/httpd/conf.d/40_mod_ssl.conf

%posttrans base
# restore lock which we disabled in pretrans
mv -f /var/lock/subsys/httpd{.disabled,} 2>/dev/null

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

# it's sooo annoying to write them
%define	module_scripts() \
%post %1 \
%module_post \
\
%postun %1 \
%module_postun

%module_scripts mod_actions
%module_scripts mod_alias
%module_scripts mod_asis
%module_scripts mod_auth_basic
%module_scripts mod_auth_dbm
%module_scripts mod_auth_digest
%module_scripts mod_authn_alias
%module_scripts mod_authn_anon
%module_scripts mod_authn_dbd
%module_scripts mod_authn_dbm
%module_scripts mod_authn_default
%module_scripts mod_authn_file
%module_scripts mod_authnz_ldap
%module_scripts mod_authz_dbm
%module_scripts mod_authz_default
%module_scripts mod_authz_groupfile
%module_scripts mod_authz_host
%module_scripts mod_authz_owner
%module_scripts mod_authz_user
%module_scripts mod_autoindex
%module_scripts mod_bucketeer
%module_scripts mod_cache
%module_scripts mod_case_filter
%module_scripts mod_case_filter_in
%module_scripts mod_cern_meta
%module_scripts mod_cgi
%module_scripts mod_cgid
%module_scripts mod_charset_lite
%module_scripts mod_dav
%module_scripts mod_dbd
%module_scripts mod_deflate
%module_scripts mod_dir
%module_scripts mod_dumpio
%module_scripts mod_echo
%module_scripts mod_env
%module_scripts mod_expires
%module_scripts mod_ext_filter
%module_scripts mod_file_cache
%module_scripts mod_filter
%module_scripts mod_headers
%module_scripts mod_ident
%module_scripts mod_imagemap
%module_scripts mod_include
%module_scripts mod_info
%module_scripts mod_ldap
%module_scripts mod_log_config
%module_scripts mod_log_forensic
%module_scripts mod_logio
%module_scripts mod_mime
%module_scripts mod_mime_magic
%module_scripts mod_negotiation
%module_scripts mod_proxy
%module_scripts mod_rewrite
%module_scripts mod_setenvif
%module_scripts mod_speling
%module_scripts mod_ssl
%module_scripts mod_status
%module_scripts mod_substitute
%module_scripts mod_unique_id
%module_scripts mod_userdir
%module_scripts mod_usertrack
%module_scripts mod_version
%module_scripts mod_vhost_alias
%module_scripts suexec

%post cgi_test
if [ "$1" = "1" ]; then
	%service -q httpd reload
fi

%postun cgi_test
if [ "$1" = "0" ]; then
	%service -q httpd reload
fi

%post errordocs
if [ "$1" = "1" ]; then
	%service -q httpd reload
fi

%postun errordocs
if [ "$1" = "0" ]; then
	%service -q httpd reload
fi

%files
%defattr(644,root,root,755)

%files base
%defattr(644,root,root,755)
%doc ABOUT_APACHE CHANGES README
%doc docs/conf/mime.types
%attr(754,root,root) /etc/rc.d/init.d/httpd
%attr(751,root,root) %dir %{_sysconfdir}
%{_sysconfdir}/modules
%{_sysconfdir}/run
%{_sysconfdir}/logs
%ghost %{_sysconfdir}/httpd.conf
%attr(750,root,root) %dir %{_sysconfdir}/conf.d
%attr(750,root,root) %dir %{_sysconfdir}/webapps.d
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_common.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mpm.conf
%attr(640,root,root) %{_sysconfdir}/magic
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/httpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*

%dir %{_libexecdir}

%attr(755,root,root) %{_sbindir}/checkgid
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/httpd.*

%dir %attr(770,root,http) /var/run/httpd
%dir %attr(770,root,http) /var/cache/httpd

%{_mandir}/man8/httpd.8*

%attr(2751,root,logs) %dir /var/log/httpd
%attr(2750,root,logs) %dir /var/log/archive/httpd
%attr(640,root,logs) %ghost /var/log/httpd/*

%dir %{_datadir}

%dir %{_datadir}/cgi-bin
%dir %{_datadir}/html
%{_datadir}/icons

%files doc -f manual.files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_manual.conf

%files errordocs
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_errordocs.conf
%{_datadir}/error

%files suexec
%defattr(644,root,root,755)
%attr(4755,root,root) %{_sbindir}/suexec
%attr(755,root,root) %{_sbindir}/suexec.fcgi
%attr(755,root,root) %{_libexecdir}/mod_suexec.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_suexec.conf
%{_mandir}/man8/suexec.8*

%files index
%defattr(644,root,root,755)
%config(noreplace,missingok) %{_datadir}/html/index.html*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/htdigest
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs
%{_mandir}/man8/ab.8*
%{_mandir}/man8/apachectl.8*
%{_mandir}/man1/htdigest.1*
%{_mandir}/man8/logresolve.8*
%{_mandir}/man8/rotatelogs.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/envvars*
%dir %{_libexecdir}
%dir %{_libexecdir}/build
%{_libexecdir}/build/[lprs]*.mk
%{_libexecdir}/build/config_vars.mk
%attr(755,root,root) %{_libexecdir}/build/*.sh
%{_includedir}
%{_mandir}/man8/apxs.8*

%files mod_actions
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_actions.conf
%attr(755,root,root) %{_libexecdir}/mod_actions.so

%files mod_alias
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_alias.conf
%attr(755,root,root) %{_libexecdir}/mod_alias.so

%files mod_asis
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_asis.conf
%attr(755,root,root) %{_libexecdir}/mod_asis.so

%files mod_auth
%defattr(644,root,root,755)

%files mod_auth_basic
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_auth_basic.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_basic.so

%files mod_auth_dbm
%defattr(644,root,root,755)

%files mod_auth_digest
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_auth_digest.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_digest.so

%files mod_authn_alias
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_alias.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_alias.so

%files mod_authn_anon
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_anon.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_anon.so

%files mod_authn_dbd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_dbd.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_dbd.so

%files mod_authn_dbm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_dbm.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_dbm.so

%files mod_authn_default
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_default.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_default.so

%files mod_authn_file
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_file.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_file.so

%if %{with ldap}
%files mod_authnz_ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authnz_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_authnz_ldap.so
%endif

%files mod_authz_dbm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_dbm.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_dbm.so

%files mod_authz_default
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_default.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_default.so

%files mod_authz_groupfile
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_groupfile.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_groupfile.so

%files mod_authz_host
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_host.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_host.so

%files mod_authz_owner
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_owner.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_owner.so

%files mod_authz_user
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_user.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_user.so

%files mod_autoindex
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_autoindex.conf
%attr(755,root,root) %{_libexecdir}/mod_autoindex.so

%if %{with bucketeer}
%files mod_bucketeer
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_bucketeer.conf
%attr(755,root,root) %{_libexecdir}/mod_bucketeer.so
%endif

%files mod_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cache.conf
%attr(755,root,root) %{_sbindir}/htcacheclean
%attr(755,root,root) %{_libexecdir}/mod_cache.so
%attr(755,root,root) %{_libexecdir}/mod_disk_cache.so
%attr(755,root,root) %{_libexecdir}/mod_mem_cache.so
%{_mandir}/man8/htcacheclean.8*

%files mod_case_filter
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_case_filter.conf
%attr(755,root,root) %{_libexecdir}/mod_case_filter.so

%files mod_case_filter_in
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_case_filter_in.conf
%attr(755,root,root) %{_libexecdir}/mod_case_filter_in.so

%files mod_cern_meta
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cern_meta.conf
%attr(755,root,root) %{_libexecdir}/mod_cern_meta.so

%files mod_cgi
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cgi.conf
%attr(755,root,root) %{_libexecdir}/mod_cgi.so

%files mod_cgid
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cgid.conf
%attr(755,root,root) %{_libexecdir}/mod_cgid.so

%files mod_charset_lite
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_charset_lite.conf
%attr(755,root,root) %{_libexecdir}/mod_charset_lite.so

%files mod_dav
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dav.conf
%attr(755,root,root) %{_libexecdir}/mod_dav*.so
%dir %attr(770,root,http) /var/lock/mod_dav

%files mod_dbd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dbd.conf
%attr(755,root,root) %{_libexecdir}/mod_dbd.so

%files mod_deflate
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_deflate.conf
%attr(755,root,root) %{_libexecdir}/mod_deflate.so

%files mod_dir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dir.conf
%attr(755,root,root) %{_libexecdir}/mod_dir.so

%files mod_dumpio
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dumpio.conf
%attr(755,root,root) %{_libexecdir}/mod_dumpio.so

%files mod_echo
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_echo.conf
%attr(755,root,root) %{_libexecdir}/mod_echo.so

%files mod_env
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_env.conf
%attr(755,root,root) %{_libexecdir}/mod_env.so

%files mod_expires
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_expires.conf
%attr(755,root,root) %{_libexecdir}/mod_expires.so

%files mod_ext_filter
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ext_filter.conf
%attr(755,root,root) %{_libexecdir}/mod_ext_filter.so

%files mod_file_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_file_cache.conf
%attr(755,root,root) %{_libexecdir}/mod_file_cache.so

%files mod_filter
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_filter.conf
%attr(755,root,root) %{_libexecdir}/mod_filter.so

%files mod_headers
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_headers.conf
%attr(755,root,root) %{_libexecdir}/mod_headers.so

%files mod_ident
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ident.conf
%attr(755,root,root) %{_libexecdir}/mod_ident.so

%files mod_imagemap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_imagemap.conf
%attr(755,root,root) %{_libexecdir}/mod_imagemap.so

%files mod_include
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_include.conf
%attr(755,root,root) %{_libexecdir}/mod_include.so

%files mod_info
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_info.conf
%attr(755,root,root) %{_libexecdir}/mod_info.so

%if %{with ldap}
%files mod_ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_ldap.so
%endif

%files mod_log_config
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_log_config.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_log_config.conf

%files mod_log_forensic
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_log_forensic.conf
%attr(755,root,root) %{_libexecdir}/mod_log_forensic.so

%files mod_logio
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_logio.conf
%attr(755,root,root) %{_libexecdir}/mod_logio.so

%files mod_mime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_mime.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_mime.conf

%files mod_mime_magic
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_mime_magic.conf
%attr(755,root,root) %{_libexecdir}/mod_mime_magic.so

%files mod_negotiation
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_negotiation.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_languages.conf
%attr(755,root,root) %{_libexecdir}/mod_negotiation.so

%files mod_proxy
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_proxy.conf
%attr(755,root,root) %{_libexecdir}/mod_proxy*.so

%files mod_rewrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/httxt2dbm
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_rewrite.conf

%files mod_setenvif
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_setenvif.conf
%attr(755,root,root) %{_libexecdir}/mod_setenvif.so

%files mod_speling
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_speling.conf
%attr(755,root,root) %{_libexecdir}/mod_speling.so

%if %{with ssl}
%files mod_ssl
%defattr(644,root,root,755)
%attr(750,root,root) %dir %{_sysconfdir}/ssl
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ssl/server.*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ssl.conf
%attr(755,root,root) %{_libexecdir}/mod_ssl.so
%endif

%files mod_status
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_status.conf
%attr(755,root,root) %{_libexecdir}/mod_status.so

%files mod_substitute
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_substitute.conf
%attr(755,root,root) %{_libexecdir}/mod_substitute.so

%files mod_unique_id
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_unique_id.conf
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so

%files mod_userdir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_userdir.conf
%attr(755,root,root) %{_libexecdir}/mod_userdir.so

%files mod_usertrack
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_usertrack.conf
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so

%files mod_version
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_version.conf
%attr(755,root,root) %{_libexecdir}/mod_version.so

%files mod_vhost_alias
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_vhost_alias.conf

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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_cgi_test.conf

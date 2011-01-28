Summary:	Spanish dictionary for aspell
Summary(es.UTF-8):	Diccionario de español para aspell
Summary(pl.UTF-8):	Hiszpański słownik dla aspella
Summary(pt_BR.UTF-8):	Dicionário de espanhol para o aspell
Name:		aspell-es
Version:	1.11
%define	subv	2
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/es/aspell6-es-%{version}-%{subv}.tar.bz2
# Source0-md5:	8406336a89c64e47e96f4153d0af70c4
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
BuildRequires:	which
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spanish dictionary (i.e. word list) for aspell.

%description -l es.UTF-8
Diccionario de la lengua española para el verificador ortográfico aspell.

%description -l pl.UTF-8
Hiszpański słownik (lista słów) dla aspella.

%description -l pt_BR.UTF-8
Dicionários da língua espanhola para o verificador ortográfico aspell.

%prep
%setup -q -n aspell6-es-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/castellano.alias
%{_libdir}/aspell/es.*
%{_libdir}/aspell/espanol.alias
%{_libdir}/aspell/spanish.alias
%{_datadir}/aspell/es.dat
%{_datadir}/aspell/es_affix.dat

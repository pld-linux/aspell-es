Summary:	Spanish dictionary for aspell
Summary(es.UTF-8):   Diccionario de español para aspell
Summary(pl.UTF-8):   Hiszpański słownik dla aspella
Summary(pt_BR.UTF-8):   Dicionário de espanhol para o aspell
Name:		aspell-es
Version:	0.50
%define	subv	2
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/es/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	4a8583e9ef9f4aed03f5a7fe09d40060
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
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
%setup -q -n %{name}-%{version}-%{subv}

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
%{_libdir}/aspell/*
%{_datadir}/aspell/*

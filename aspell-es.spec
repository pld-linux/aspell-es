Summary:	Spanish dictionary for aspell
Summary(pl):	Hiszpa�ski s�ownik dla aspella
Summary(pt_BR):	Dicion�rio de espanhol para o aspell
Name:		aspell-es
Version:	0.50
%define	subv	2
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/es/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	4a8583e9ef9f4aed03f5a7fe09d40060
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spanish dictionary (i.e. word list) for aspell.

%description -l pl
Hiszpa�ski s�ownik (lista s��w) dla aspella.

%description -l pt_BR
Dicion�rios da l�ngua espanhola para o verificador ortogr�fico aspell.

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

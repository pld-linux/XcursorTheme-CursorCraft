%define		_name CursorCraft
Summary:	A cursor theme based on cursors from Starcraft game.
Summary(pl):	Motyw kursorów oparty na kursorach z gry Starcraft.
Name:		XcursorTheme-%{_name}
Version:	0.2
Release:	1
License:	Free for noncommercial use
Group:		Themes
Source0:	http://www.kde-look.org/content/files/5377-%{_name}-%{version}.tar.bz2
# Source0-md5:	20eb545c823ce14bf9b85eb755543b0e
URL:		http://www.kde-look.org/content/show.php?content=5377
BuildRequires:	XFree86 >= 4.3
Buildarch:	noarch
Requires:	XFree86 >= 4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Green, future-looking cursors resembling the ones from Starcraft.

%description -l pl
Zielone kursory podobne do tych z gry Starcraft.

%prep
%setup -q -n %{_name}-%{version}

%build
head -n 42 install.sh > build.sh
chmod +x ./build.sh
./build.sh

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors
cp -df ./cursors/*  $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors/

echo "[Icon Theme]" > $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme
echo "Name = CursorCraft" >> $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme
echo "Comment = A cursor theme inspired from the Starcraft game" >> $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}
